
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

start_marker = '<div class="logo-parent-w">'
matches = []
idx = 0
while True:
    idx = content.find(start_marker, idx)
    if idx == -1:
        break
    end_idx = find_div_end(content, idx + len(start_marker))
    block_content = content[idx:end_idx]
    
    # Check if this block contains old logos
    if "Reddot" in block_content or "Deutscher" in block_content or "Made-in-lux" in block_content:
        print(f"Found old logo block at {idx}. Mark for deletion.")
        matches.append((idx, end_idx))
    else:
        print(f"Keeping block at {idx} (seems to be new or other).")
        
    idx = end_idx

if matches:
    # Delete match. Iterate backwards.
    new_content = content
    for start, end in reversed(matches):
        new_content = new_content[:start] + new_content[end:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Deleted old logo blocks.")
else:
    print("No old logo blocks found to delete.")
