
# Fixing broken images.
# Valid files found: new_member_1.jpg, etc.
# Mapping:
# Arnpreet -> new_member_1.jpg
# Bishal -> new_member_2.jpg
# Ambatokandh -> new_member_3.jpg
# Rapunzal -> new_member_4.jpg

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacements
replacements = {
    'assets/team_arnpreet.jpg': 'assets/new_member_1.jpg',
    'assets/team_bishal.jpg': 'assets/new_member_2.jpg',
    'assets/team_ambatokandh.jpg': 'assets/new_member_3.jpg',
    'assets/team_rapunzal.jpg': 'assets/new_member_4.jpg'
}

for old, new in replacements.items():
    if old in html:
        print(f"Replacing {old} with {new}")
        html = html.replace(old, new)
    else:
        print(f"Warning: Could not find {old} in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
