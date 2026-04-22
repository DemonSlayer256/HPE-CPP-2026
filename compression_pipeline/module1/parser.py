import os, re, json, uuid
from multiprocessing import Pool, cpu_count
from markdown_it import MarkdownIt

BAD_SUBJECTS = {"you","we","it","they","this","that","who","which"}
BAD_OBJECTS = {"value","data","object","thing","information","example"}
BAD_VERBS = {"be","have","do","make","use","is","are","was","were","has","had","can","could","will","would","should","may","might","set","get","list","create","delete"}

DOMAIN_TERMS = {
    "aws","s3","bucket","object","header","request","response",
    "encryption","kms","policy","api","endpoint","session","checksum"
}

def load_md(p):
    text = open(p,"r",encoding="utf-8").read()
    # remove lines with many dots (TOC)
    text = re.sub(r".*\.{10,}.*\n", "", text)
    # remove API Version lines
    text = re.sub(r"API Version \d{4}-\d{2}-\d{2}.*\n", "", text)
    # remove page headers
    text = re.sub(r"^Amazon Simple Storage Service API Reference\n", "", text, flags=re.MULTILINE)
    # remove copyright
    text = re.sub(r"Copyright © \d+ Amazon Web Services.*\n", "", text)
    # remove trademarks
    text = re.sub(r"Amazon's trademarks.*\n", "", text)
    return text

def parse_md(text):
    md = MarkdownIt()
    tokens = md.parse(text)
    sections = []
    stack = []
    current = {"heading_path":[],"content":[],"section_id":str(uuid.uuid4())}

    i = 0
    while i < len(tokens):
        t = tokens[i]

        if t.type == "heading_open":
            level = int(t.tag[1])
            title = tokens[i+1].content.strip()

            if current["content"]:
                sections.append({
                    "section_id": current["section_id"],
                    "heading_path": current["heading_path"],
                    "content": " ".join(current["content"])
                })
                current = {"heading_path":stack[:level-1] + [title],"content":[],"section_id":str(uuid.uuid4())}

            stack = stack[:level-1] + [title]
            i += 2

        elif t.type == "paragraph_open":
            content = tokens[i+1].content.strip()
            current["content"].append(content)
            i += 2

        elif t.type == "inline" and t.content.strip():
            current["content"].append(t.content.strip())
            i += 1

        elif t.type == "bullet_list_open":
            items = []
            i += 1
            while tokens[i].type != "bullet_list_close":
                if tokens[i].type == "inline":
                    items.append(tokens[i].content.strip())
                i += 1
            if items:
                current["content"].append(" ".join(items))
            i += 1

        else:
            i += 1

    if current["content"]:
        sections.append({
            "section_id": current["section_id"],
            "heading_path": current["heading_path"],
            "content": " ".join(current["content"])
        })

    return sections

def clean_text(t):
    t = re.sub(r"\s+"," ",t)
    t = re.sub(r"Note .*?\.","",t)
    t = re.sub(r"Important .*?\.","",t)
    return t.strip()

def split_sentences(t):
    return re.split(r'(?<=[.!?])\s+', t)

def valid_sentence(s):
    w = s.split()
    if len(w) < 8 or len(w) > 35: return False
    if s.strip().startswith(("•","-","*")): return False
    return True

def build_chunks(sections):
    chunks, cid = [], 0

    for sec in sections:
        text = clean_text(sec["content"])
        sents = [s for s in split_sentences(text) if valid_sentence(s)]

        cur = []
        for s in sents:
            cur.append(s)
            if len(" ".join(cur).split()) > 500:
                chunk = " ".join(cur)
                if len(chunk.split()) >= 200:
                    chunks.append({
                        "chunk_id": f"c{cid}",
                        "text": chunk,
                        "tokens": len(chunk.split()),
                        "heading_path": sec["heading_path"],
                        "section_id": sec["section_id"],
                        "source": "",
                        "position": cid
                    })
                    cid += 1
                cur = []

        if cur:
            chunk = " ".join(cur)
            if len(chunk.split()) >= 200:
                chunks.append({
                    "chunk_id": f"c{cid}",
                    "text": chunk,
                    "tokens": len(chunk.split()),
                    "heading_path": sec["heading_path"],
                    "section_id": sec["section_id"],
                    "source": "",
                    "position": cid
                })
                cid += 1

    return chunks

def expand_np(tok):
    return " ".join([t.text for t in tok.subtree if not t.is_punct][:6])

def is_domain_phrase(t):
    tl = t.lower()
    return any(d in tl for d in DOMAIN_TERMS)

def valid_aku(s,v,o):
    s_l, o_l = s.lower(), o.lower()

    if s_l in BAD_SUBJECTS or o_l in BAD_OBJECTS: return False
    if v in BAD_VERBS: return False
    if len(s.split()) > 6 or len(o.split()) > 6: return False
    if len(s.split()) < 2 or len(o.split()) < 2: return False
    if any(char.isdigit() for char in s + o + v): return False
    if not (is_domain_phrase(s) or is_domain_phrase(o)): return False
    return True

def extract_akus(text):
    try:
        nlp
    except NameError:
        import spacy
        nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    akus = []

    for sent in doc.sents:
        for tok in sent:
            if tok.pos_ == "VERB":
                subs, objs = [], []

                for c in tok.children:
                    if c.dep_ in ("nsubj","nsubjpass"):
                        subs.append(expand_np(c))
                    if c.dep_ in ("dobj","pobj","attr"):
                        objs.append(expand_np(c))

                for s in subs:
                    for o in objs:
                        if valid_aku(s, tok.lemma_, o):
                            akus.append([s, tok.lemma_, o])

    seen = set()
    out = []
    for a in akus:
        k = tuple([w.lower() for w in a])
        if k not in seen:
            seen.add(k)
            out.append(a)

    return out

def process_chunk(args):
    cid, txt = args
    akus = extract_akus(txt)
    return {"chunk_id": cid, "akus": akus}

def parallel_aku(chunks):
    return [process_chunk((c["chunk_id"], c["text"])) for c in chunks]

def run(input_path, output_dir):
    raw = load_md(input_path)
    sections = parse_md(raw)
    chunks = build_chunks(sections)
    # add overlap
    for i in range(1, len(chunks)):
        prev_words = chunks[i-1]["text"].split()
        overlap_words = prev_words[-100:] if len(prev_words) >= 100 else prev_words
        overlap = " ".join(overlap_words)
        chunks[i]["text"] = overlap + " " + chunks[i]["text"]
        chunks[i]["tokens"] = len(chunks[i]["text"].split())
    akus = parallel_aku(chunks)
    akus = [a for a in akus if a["akus"]]

    os.makedirs(output_dir, exist_ok=True)
    json.dump(chunks, open(os.path.join(output_dir,"chunks.json"),"w"), indent=2)
    json.dump(akus, open(os.path.join(output_dir,"akus.json"),"w"), indent=2)

    print(f"Done | Chunks: {len(chunks)} | AKUs: {sum(len(a['akus']) for a in akus)}")

if __name__ == "__main__":
    run("../../data/prototype/S3/L0/s3-api.md","s3/intermediate")