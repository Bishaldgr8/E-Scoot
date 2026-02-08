
# Forgot to import re. Sorry.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

indices = [m.start() for m in re.finditer('marquee-container', html)]
print(f"Found {len(indices)} occurrences at: {indices}")

if indices:
    # Print the first instance context
    start = indices[0]
    print("--- First Instance ---")
    print(html[max(0, start-100):start+500])
    
    if len(indices) > 1:
        start2 = indices[1]
        print("--- Second Instance ---")
        print(html[max(0, start2-100):start2+500])
