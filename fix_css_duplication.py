
# Removing ALL duplicate .swiper-slide CSS blocks.
# And inserting ONE single source of truth.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove ALL .swiper-slide blocks.
# Regex: `\.swiper-slide\s*\{[^}]*\}`
# I'll use a loop to be sure, or re.sub with count=0 (default).

pattern = re.compile(r'\.swiper-slide\s*\{[^}]*\}', re.DOTALL)

# Count matches first for debug.
matches = pattern.findall(html)
print(f"Removing {len(matches)} conflicting CSS blocks.")

html = pattern.sub('', html)

# 2. Insert the correct CSS.
# I'll put it right before </head>.

new_css = '''
<style>
/* Final Swiper Fix */
.swiper-slide {
    width: 22% !important; 
    margin-right: 2% !important;
    box-sizing: border-box;
    height: auto !important;
    opacity: 1 !important; /* Ensure visibility */
    display: block !important;
}
.swiper-slide img {
    width: 100% !important;
    height: auto !important;
    object-fit: cover;
}
/* Ensure wrapper doesn't force width */
.swiper-wrapper {
    box-sizing: border-box;
}
</style>
'''

html = html.replace('</head>', new_css + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
