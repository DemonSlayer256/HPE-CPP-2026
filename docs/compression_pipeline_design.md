
# Compression Pipeline Design

## 1. Overview
This document describes the design of an AWS Knowledge Compression Pipeline. The system transforms raw documentation into structured, compact, and reliable knowledge representations.

Rather than simply summarizing text, the pipeline focuses on preserving facts while progressively compressing information. This ensures that even highly compressed outputs remain accurate and meaningful.

### 1.1 Pipeline Structure
The system is organized into three core modules:
1. Document Chunking
2. Topic Extraction
3. Hierarchical Summarization

Each module builds on the output of the previous one, gradually increasing structure while reducing redundancy.

### 1.2 Data Flow
The pipeline operates as a sequential transformation:
- Chunking produces structured chunks enriched with metadata and atomic facts
- Topic extraction organizes these facts into a knowledge graph
- Summarization compresses this structured representation into multiple levels

### 1.3 System Objectives
The system is designed to:
- Preserve critical factual information
- Represent knowledge in a structured and connected form
- Enable scalable compression across different abstraction levels


## 2. Module 1: Document Chunking
This module prepares raw documents for downstream processing by dividing them into meaningful, manageable units.

### 2.1 Chunking Strategy
Documents are split using natural structural boundaries such as headings. When sections are too large, they are further divided using paragraph-level splitting.

- Typical chunk size ranges between 500 and 1000 tokens  
- Splitting respects semantic coherence and document structure  

This ensures each chunk remains meaningful and self-contained.

### 2.2 Overlap Strategy
To preserve context across boundaries, overlap is introduced between consecutive chunks.

- Each chunk shares the last 100 tokens with the next  

This prevents loss of context and maintains continuity of entities and ideas.

### 2.3 Metadata
Each chunk is enriched with contextual metadata, including:
- Its position within the document  
- Section hierarchy  
- Source reference  

This enables traceability, contextual reconstruction, and consistency across stages.

### 2.4 Atomic Knowledge Unit (AKU) Extraction
After chunking, each chunk is further decomposed into Atomic Knowledge Units (AKUs).

#### 2.4.1 Definition
An AKU represents the smallest self-contained factual statement.

Each AKU follows a structured form:
- Subject → Predicate → Object  

Example:  
"AWS Lambda requires an IAM role"  
→ (Lambda, requires, IAM Role)

#### 2.4.2 Properties
A valid AKU is:
- Self-contained  
- Focused on a single fact or action  
- Explicitly tied to entities  
- Interpretable as a standalone unit  

#### 2.4.3 Role in the System
AKUs form the foundational layer of the pipeline. They capture facts independently of how they are written in the source.

They are used to:
- Preserve factual correctness during compression  
- Guide summarization  
- Enable validation  
- Maintain consistency across outputs  

#### 2.4.4 Integration
AKUs are generated immediately after chunking, stored alongside chunks, and carried through all downstream modules.


## 3. Module 2: Topic Extraction
This module organizes extracted information into a structured representation by identifying entities, relationships, and themes.

### 3.1 Core Functions
The module performs:
- Topic identification  
- Entity extraction  
- Relationship mapping  
- Importance estimation  

### 3.2 Knowledge Graph Construction
The output of this module is a knowledge graph:
- Nodes represent entities (services, components, configurations)  
- Edges represent relationships between them  

This graph captures how different parts of the system interact.

### 3.3 Graph-Guided Processing
The knowledge graph plays an active role in downstream stages.

It is used to:
- Identify important entities  
- Preserve key relationships  
- Guide the summarization process  

### 3.4 Importance-Driven Representation
The system evaluates importance based on:
- Frequency of occurrence  
- Structural position within documents  
- Connectivity within the graph  

This determines which information is prioritized and retained during compression.


## 4. Module 3: Hierarchical Summarization
This module performs progressive compression of information into multiple levels of abstraction.

### 4.1 Hierarchical Structure

| Level | Scope |
|------|------|
| Level 4 | Section summaries |
| Level 3 | Document summaries |
| Level 2 | Topic summaries |
| Level 1 | Category summaries |
| Level 0 | Global overview |

### 4.2 Aggregation Flow
Each level is built from the level directly below it:

Sections → Documents → Topics → Categories → Global  

This ensures that higher-level summaries remain grounded in lower-level information.

### 4.3 Progressive Compression
- Lower levels retain detailed technical information  
- Higher levels focus on abstraction and clarity  

This enables different levels of detail depending on user needs.

### 4.4 Token Budgets

| Level | Approx Tokens |
|------|--------------|
| Section | ~500 |
| Document | ~200 |
| Topic | ~100 |
| Category | ~50 |
| Global | ~25 |

These budgets guide how aggressively information is compressed at each level.

### 4.5 Constraint-Based Summarization
Summarization is guided by structured constraints to ensure factual integrity.

- Important entities must be included  
- Key relationships must be preserved  
- Numerical values must remain exact  
- AKUs act as anchors for factual correctness  

This reduces hallucination and ensures reliable outputs.

### 4.6 Cross-Level Consistency
Consistency is maintained across all levels of the hierarchy.

- The same facts should persist across summaries  
- AKUs and shared entities link different levels  

This ensures coherence and prevents contradictions.

### 4.7 Validation
The system includes validation mechanisms to maintain quality.

- Summaries are checked against AKUs  
- Unsupported or hallucinated information is identified  
- Coverage of important entities and relationships is verified  

This ensures that compression does not compromise accuracy.


## 5. System Characteristics

### 5.1 Summary
The system provides:
- Fact-preserving compression of knowledge  
- Structured representation through a knowledge graph  
- Scalable hierarchical summarization  
- Consistent and interpretable outputs  
