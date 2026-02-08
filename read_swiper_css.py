
# Debugging why CSS isn't taking effect.
# I'll print all occurrences of `.swiper-slide` in index.html.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Total length: {len(html)}")

# Find all matches of .swiper-slide definition
matches = re.findall(r'(\.swiper-slide\s*\{[^}]*\})', html, re.DOTALL)
print(f"Found {len(matches)} CSS blocks for .swiper-slide:")
for i, m in enumerate(matches):
    print(f"--- Block {i+1} ---")
    print(m)
    print("----------------")

# Also check for inline styles on the elements themselves (in case Swiper added them in HTML source?)
# Swiper adds them at runtime, so they won't be in the file unless saved from browser.
# But I should check the HTML markup for `style="..."`.

inline_styles = re.findall(r'<div[^>]*class="[^"]*swiper-slide[^"]*"[^>]*style="([^"]*)"', html)
if inline_styles:
    print(f"Found {len(inline_styles)} swiper-slides with inline styles:")
    for s in inline_styles[:3]:
        print(s)
