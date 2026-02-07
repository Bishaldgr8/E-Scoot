
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the marquee position
marquee_idx = content.find('<div class="logo-marquee">')

if marquee_idx != -1:
    print(f"Found marquee at {marquee_idx}")
    
    # Look backwards for any logo-parent divs before the marquee
    # These would be the static duplicates we want to remove
    
    # Search for logo-parent divs in the 5000 chars before marquee
    search_start = max(0, marquee_idx - 5000)
    preceding = content[search_start:marquee_idx]
    
    # Find all logo-parent divs
    logo_parent_matches = list(re.finditer(r'<div class="logo-parent[^"]*"[^>]*>.*?</div>', preceding, re.DOTALL))
    
    if logo_parent_matches:
        print(f"Found {len(logo_parent_matches)} logo-parent divs before marquee")
        
        # Remove all of them by working backwards
        new_content = content
        for match in reversed(logo_parent_matches):
            # Adjust indices to absolute position
            abs_start = search_start + match.start()
            abs_end = search_start + match.end()
            print(f"Removing logo-parent at {abs_start}-{abs_end}")
            new_content = new_content[:abs_start] + new_content[abs_end:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Removed duplicate logo blocks.")
    else:
        print("No logo-parent divs found before marquee.")
else:
    print("Marquee not found.")
