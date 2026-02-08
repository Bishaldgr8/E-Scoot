
# User says "not taking effect".
# CSS classes might be overridden or ignored.
# I will INJECT INLINE STYLES into the HTML elements themselves.
# This forces the browser to obey.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Regex to match swiper-slide divs.
# <div ... class="...swiper-slide..." ... >
# I need to insert `style="width: 22% !important; margin-right: 2% !important;"`
# If style attribute exists, append to it.
# If not, create it.

# Pattern approach:
# Find whole tag: `<div[^>]*class="[^"]*swiper-slide[^"]*"[^>]*>`
# This is tricky with regex.
# Better to use string replacement if possible?
# But attributes order varies.

# I'll use a callback function with re.sub.
# Match `<div ... class="...swiper-slide..." ...>`
# Note: "class" might trigger before or after "style".

def add_inline_style(match):
    tag = match.group(0)
    
    # Check if style exists
    if 'style="' in tag:
        # Append to existing style.
        # Replace `style="...` with `style="width: 22% !important; margin-right: 2% !important; ...`
        # OR just append inside the quote.
        tag = re.sub(r'style="([^"]*)"', r'style="width: 22% !important; margin-right: 2% !important; \1"', tag)
    else:
        # Add style attribute.
        tag = tag.replace('<div', '<div style="width: 22% !important; margin-right: 2% !important;"')
        
    return tag

# Construct Regex.
# Matches: <div followed by anything until class="...swiper-slide..." followed by anything until >
# This is risky if > is inside quotes. Assuming standard HTML.
# Pattern: `<div(?=\s)(?=(?:[^>"']|"[^"]*"|'[^']*')*?\sclass="[^"]*swiper-slide[^"]*")(?:[^>"']|"[^"]*"|'[^']*')*>`
# Simplified: `<div[^>]*class="[^"]*swiper-slide[^"]*"[^>]*>` (Greedy match warning!)
# non-greedy match for content inside tag.

pattern = re.compile(r'<div\s+(?:[^>]*?\s+)?class="[^"]*swiper-slide[^"]*"[^>]*>', re.IGNORECASE)

# Test count
matches = pattern.findall(html)
print(f"Found {len(matches)} swiper-slide tags to patch.")

fixed_html = pattern.sub(add_inline_style, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(fixed_html)
