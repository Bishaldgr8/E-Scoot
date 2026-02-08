
# Findings:
# Marquee Containers: 2 !! (Wait, I thought I deleted them?)
# make_in_india.svg: 2
# iiit_una_logo.png: 5 (Why 5??)
# govt_of_india.png: 5
# digital_india.svg: 5
# swachh_bharat.svg: 3 (Why 3??)
# made_in_india.svg: 5

# This is a mess.
# There are 5 sets of some icons?
# And 2 Marquee containers.
# And 3 Swachh Bharat?

# I must have:
# 1. Original Set (Maybe 1 copy of some?)
# 2. My "Static Set" (Maybe I deleted it partially?)
# 3. Marquee 1 (12 items? No wait. 2 items of each type * 2 sets = 4? No. 2 sets in marquee = 2 of each.)
# If I have 2 Marquees, I should have 4 of each.
# Counts are 5, 3, 2.
# This means broken HTML.

# ACTION:
# I will REMOVE ALL instances of these images from the footer area.
# I will locate the Footer area and WIPE IT CLEAN of these specific images.
# Then Insert ONE Marquee.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Marquee Containers (Again, but better).
# Finds all `<div class="marquee-container">...</div></div>` blocks.
# I'll use the parser I wrote, but ensure it finds ALL.

def remove_marquees(html_content):
    while True:
        start = html_content.find('<div class="marquee-container">')
        if start == -1:
            break
        # Find end using depth default logic or just a heuristic if depth fails.
        # Structure is known: <div class="marquee-container">...</div>
        # But wait, earlier inspection showed `</div></div>` at end?
        # My previous parser relied on structure.
        
        # Let's verify context first.
        # print("Found marquee at", start)
        
        # Simple removal: Remove from `start` to next `</body>`? No.
        # Remove from `start` until `</div>` that closes it.
        
        # Use simple count.
        current = start + 1
        depth = 1
        end = -1
        while current < len(html_content):
            n_o = html_content.find('<div', current)
            n_c = html_content.find('</div>', current)
            if n_c == -1: break
            
            if n_o != -1 and n_o < n_c:
                depth += 1
                current = n_o + 4
            else:
                depth -= 1
                current = n_c + 6
                if depth == 0:
                    end = current
                    break
        
        if end != -1:
            # print(f"Removing marquee block {start}:{end}")
            html_content = html_content[:start] + html_content[end:]
        else:
            print("Could not parse marquee end. Force remove common structure?")
            # If parser fails, regex?
            # Or just hack: find `<!-- Set 2 -->` and cut around it?
            break
    return html_content

html = remove_marquees(html)
print("Removed marquees via parser.")

# 2. Remove Stray Icons.
# I will remove any `img` tag with `src="assets/make_in_india.svg"` etc.
# But ONLY if they are not in the Marquee (which is gone now).
# So I can safety remove ALL occurrences of these specific footer assets.
# EXCEPT if they are used elsewhere (Header?).
# User said "add more govt... icons". They shouldn't be in header.
# "IIIT Una Logo" might be in header?
# `assets/iiit_una_logo.png` -> Inspect header to be sure.
# The map might use it? No.
# Header usually has `logo.svg` or `escoot.png`.

# I will verify if `iiit_una_logo.png` is used in Header.
if 'header' in html.lower():
    # check first 2000 chars
    head_part = html[:3000]
    if 'iiit_una_logo.png' in head_part:
        print("Warning: IIIT Una logo found in header. Skipping global delete for it.")
    else:
        print("IIIT Una logo not in header. Safe to delete.")

# List of assets to wipe
assets_to_wipe = [
    'assets/make_in_india.svg',
    'assets/govt_of_india.png',
    'assets/digital_india.svg',
    'assets/swachh_bharat.svg',
    'assets/made_in_india.svg'
]
# Exclude IIIT Una for now unless I'm sure. `assets/iiit_una_logo.png`

for asset in assets_to_wipe:
    # Regex to find whole tag: <img ... src="asset" ... >
    # `[^>]*` matches attributes.
    p = re.compile(f'<img[^>]*src="{asset}"[^>]*>', re.IGNORECASE)
    html = p.sub('', html)

# Wipe IIIT Una if not in header?
# I'll rely on the marquee insertion to put them back.
# So I want to remove OLD ones.
# previous logic checked header.
if 'iiit_una_logo.png' not in html[:3000]:
    p = re.compile(r'<img[^>]*src="assets/iiit_una_logo.png"[^>]*>', re.IGNORECASE)
    html = p.sub('', html)

print("Wiped duplicate icons.")

# 3. Clean up empty containers?
# `footer-logo-grid` or wrappers might remain empty.
# Regex to remove empty divs? `<div class="...">\s*</div>`
# Might be risky. Leave them.

# 4. Insert ONE Clean Marquee.
marquee_html = '''
<div class="marquee-container">
    <div class="marquee-content">
        <!-- Set 1 -->
        <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India" style="height: 90px;"></div>
        <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
        
        <!-- Set 2 -->
        <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India" style="height: 90px;"></div>
        <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
    </div>
</div>
'''

html = html.replace('</body>', marquee_html + '\n</body>')
print("Inserted fresh marquee.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
