
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

# New logos
logos = [
    {"src": "assets/govt_of_india.png", "alt": "Government of India", "width": "80"},
    {"src": "assets/iiit_una_logo.png", "alt": "IIIT Una", "width": "100"},
    {"src": "assets/make_in_india.svg", "alt": "Make in India", "width": "120"},
    {"src": "assets/swachh_bharat.svg", "alt": "Swachh Bharat", "width": "120"},
    {"src": "assets/digital_india.svg", "alt": "Digital India", "width": "120"},
    {"src": "assets/made_in_india.svg", "alt": "Made in India", "width": "120"}
]

# Generate new HTML block content
new_inner_html = ""
for logo in logos:
    new_inner_html += f'<div class="logo-parent pr-60 width-240"><img src="{logo["src"]}" width="{logo["width"]}" alt="{logo["alt"]}"/></div>'

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Regex to find <div class="logo-parent-w">...</div>
# This is tricky with regex due to nested divs.
# However, the structure seems flat: <div class="logo-parent-w"> <div class="logo-parent ...">...</div> ... </div>
# I will use a non-greedy match but need to be careful.

# Given the specific structure seen in previous output, 
# I'll rely on finding the start tag and the next `</div></div>` which likely closes the logo row and its parent container if structured that way.
# Or simpler: find `<div class="logo-parent-w">` and replace everything until the *next* `<div class="logo-parent-w">` or some other marker?
# Actually, there are TWO logo rows usually. I should replace both or just one and delete the other?
# Or replace all instances.

# Let's try to find the block by knowing what's inside.
# Inside are `class="logo-parent ..."` divs.

pattern = re.compile(r'<div class="logo-parent-w">.*?</div></div>', re.DOTALL)
# This regex might be too aggressive or too weak.

# Alternative approach: Locate start of logo-parent-w, find matching closing div by counting.
def find_div_end(s, start_idx):
    count = 1
    i = start_idx + 1
    while count > 0 and i < len(s):
        if s[i:i+4] == '<div':
            count += 1
            i += 4
        elif s[i:i+6] == '</div>':
            count -= 1
            i += 6
        else:
            i += 1
    return i

start_marker = '<div class="logo-parent-w">'
matches = []
idx = 0
while True:
    idx = content.find(start_marker, idx)
    if idx == -1:
        break
    end_idx = find_div_end(content, idx + len(start_marker))
    matches.append((idx, end_idx))
    idx = end_idx

if matches:
    print(f"Found {len(matches)} blocks.")
    # Replace them. Iterate backwards to keep indices valid.
    new_content = content
    for start, end in reversed(matches):
        # Construct the full replacement block
        replacement = f'<div class="logo-parent-w">{new_inner_html}</div>'
        new_content = new_content[:start] + replacement + new_content[end:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Replaced logo blocks.")
else:
    print("No logo blocks found.")
