
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# Find ALL occurrences of social icons with their context
pattern = r'<div class="social-txt-1">([^<]*)</div>'
matches = list(re.finditer(pattern, content))

print(f"Found {len(matches)} social icon instances:\n")

for i, match in enumerate(matches, 1):
    text = match.group(1)
    pos = match.start()
    
    # Get context - 200 chars before and after
    start = max(0, pos - 200)
    end = min(len(content), pos + 200)
    context = content[start:end]
    
    # Find the href in this context
    href_match = re.search(r'href="([^"]*)"', context)
    href = href_match.group(1) if href_match else "NO HREF FOUND"
    
    print(f"{i}. Text: '{text}' | Position: {pos}")
    print(f"   URL: {href}")
    print(f"   Context snippet: ...{context[max(0, pos-start-50):pos-start+50]}...")
    print()
