
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

# The unique part identifying the map anchor
target_snippet = 'assets/map_iiit_una.png'

iframe_code = '<iframe src="https://maps.google.com/maps?q=31.481124,76.190682&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>'

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Locate the anchor tag containing the target snippet
# We can find the start of the <a> tag before the snippet and the end </a> after it.
# The structure is <a ... data-bg="assets/map_iiit_una.png" ... > ... </a>

# Find the snippet index
idx = content.find(target_snippet)
if idx == -1:
    print("Could not find the map image snippet.")
else:
    # Find the start of the <a> tag
    start_tag_idx = content.rfind('<a', 0, idx)
    
    # Find the end of the </a> tag
    end_tag_idx = content.find('</a>', idx)
    
    if start_tag_idx != -1 and end_tag_idx != -1:
        end_tag_idx += 4 # Include </a>
        
        original_tag = content[start_tag_idx:end_tag_idx]
        print(f"Found tag: {original_tag[:100]}...")
        
        # Replace
        new_content = content[:start_tag_idx] + iframe_code + content[end_tag_idx:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Replacement successful.")
    else:
        print("Could not locate the full anchor tag boundaries.")
