
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

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

keywords = ["Reddot", "Deutscher", "Made-in-lux", "ANDYs", "Design In Germany", "Designed in germany"]

while True:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    found_keyword = None
    keyword_idx = -1
    for kw in keywords:
        k_idx = content.find(kw)
        if k_idx != -1:
            found_keyword = kw
            keyword_idx = k_idx
            break
    
    if found_keyword:
        print(f"Found keyword '{found_keyword}' at {keyword_idx}")
        # Find container start
        start_marker = '<div class="logo-parent-w">'
        container_start = content.rfind(start_marker, 0, keyword_idx)
        
        if container_start != -1:
            # Find end
            container_end = find_div_end(content, container_start + len(start_marker))
            print(f"Removing block {container_start}-{container_end}")
            
            # Remove
            new_content = content[:container_start] + content[container_end:]
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Removed block. Checking again...")
        else:
            print("Could not find container start for keyword! Manual intervention needed?")
            break
    else:
        print("No old keywords found.")
        break
