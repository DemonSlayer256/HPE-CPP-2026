import os
import json
import shutil

def organize_raw_data():
    raw_dir = 'raw'
    prototype_dir = 'data/prototype'
    manifest_path = 'manifest.json'

    # Load the manifest
    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    # Process each file in the manifest
    for item in manifest['files']:
        filename = item['filename']
        service = item['service']
        layer = item['layer']
        
        # Source and destination paths
        src_path = os.path.join(raw_dir, filename)
        dest_dir = os.path.join(prototype_dir, service, layer)
        dest_path = os.path.join(dest_dir, filename)

        if os.path.exists(src_path):
            # Create the nested directories if they don't exist
            os.makedirs(dest_dir, exist_ok=True)
            # Copy (or move) the file
            shutil.copy2(src_path, dest_path)
            print(f"Moved {filename} -> {dest_dir}/")
        else:
            print(f"Warning: {filename} not found in {raw_dir}/")

if __name__ == "__main__":
    organize_raw_data()