
# Finding where "Arnpreet" lives.
# Searching all HTML files.

import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Scanning {len(html_files)} HTML files for 'Arnpreet'...")

found = False
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Arnpreet' in content:
        print(f"MATCH: Found 'Arnpreet' in {fname}!")
        if 'swiper-container' in content:
            print(f"  - And it has a Swiper container.")
        if 'width: 279px' in content:
            print(f"  - It still has the OLD width constraint!")
        found = True

if not found:
    print("Arnpreet not found in any HTML file. (Is it JS injected?)")
