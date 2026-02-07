
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# Replace >FB< with >GH<
original_content = content
content = content.replace('>FB<', '>GH<')

if content != original_content:
    print("Replaced >FB< with >GH<")
else:
    print("No >FB< found to replace")

original_content = content

# Remove any element containing >IG<
# Find the pattern and remove the entire anchor tag
ig_pattern = r'<a[^>]*>.*?>IG<.*?</a>'
content = re.sub(ig_pattern, '', content, flags=re.DOTALL)

if content != original_content:
    print("Removed >IG< element")
else:
    print("No >IG< found to remove")

# Also update any facebook.com URLs to github
content = content.replace('facebook.com/ujetofficial', 'github.com/Bishaldgr8')

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\nAll replacements complete!")

# Verify
if '>FB<' in content:
    print("WARNING: >FB< still exists!")
else:
    print("✓ No >FB< found")
    
if '>IG<' in content:
    print("WARNING: >IG< still exists!")
else:
    print("✓ No >IG< found")
