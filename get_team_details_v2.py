
# Extract Image Sources and Roles for Team Members.
# I will search for the blocks containing the names.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Names to search
names = ["Arnpreet Y", "Bishal B", "Ambatokandh Singh", "Rapunzal S"]

for name in names:
    print(f"--- Searching for {name} ---")
    # Find the block roughly.
    # Find index of name.
    idx = html.find(name)
    if idx != -1:
        # Look backwards for <img src="...">
        # Look forwards for Role.
        
        # Snippet around name
        start = max(0, idx - 500)
        end = min(len(html), idx + 500)
        snippet = html[start:end]
        
        # Find image in snippet.
        img_match = re.search(r'<img[^>]*src="([^"]*)"', snippet)
        if img_match:
            print(f"Image: {img_match.group(1)}")
        else:
            print("Image not found in snippet.")
            
        # Find Role (surrounding divs/h4s).
        # Role is usually after name? Or before?
        # Print snippet for manual verification if regex fails.
        # Clean up newlines.
        clean_snippet = snippet.replace('\n', ' ').replace('\r', '')
        print(f"Context: {clean_snippet[:200]} ... {clean_snippet[-200:]}")
    else:
        print(f"Name {name} not found.")
