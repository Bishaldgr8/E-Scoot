
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Helper to find matching closing div
def find_div_end(s, start_idx):
    count = 1
    i = start_idx + 1
    while count > 0 and i < len(s):
        if s[i:i+4] == '<div':
            count += 1
            i += 4
        elif s[i:i+6] == '</div>':
            count -= 1
            i += 6
        else:
            i += 1
    return i

# Find "Reddot"
target = "Reddot"
idx = content.find(target)

if idx != -1:
    print(f"Found '{target}' at {idx}")
    
    # Find start of container before this index
    start_marker = '<div class="logo-parent-w">'
    # rfind (reverse find) from 0 to idx
    container_start = content.rfind(start_marker, 0, idx)
    
    if container_start != -1:
        print(f"Found container start at {container_start}")
        container_end = find_div_end(content, container_start + len(start_marker))
        
        print(f"Identified block from {container_start} to {container_end}")
        print("Block content preview (start):", content[container_start:container_start+100])
        print("Block content preview (end):", content[container_end-100:container_end])
        
        # Verify it contains Reddot (sanity check)
        if target in content[container_start:container_end]:
            # Remove it
            new_content = content[:container_start] + content[container_end:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully removed old logo block.")
        else:
            print("Error: Identified block does not contain target! Aborting.")
    else:
        print("Could not find container start before signal.")
else:
    print(f"'{target}' not found.")
