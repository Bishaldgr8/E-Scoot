
# User says "you didnt delete this belt".
# I suspect there are still duplicate icons (Static ones).
# I count if > 12 (Marquee has 2 sets of 6 = 12).

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = html.count('assets/make_in_india.svg')
print(f"Total Make in India icons: {count}")

# Check for specific containers
if 'footer-static-icons' in html:
    print("Found 'footer-static-icons' container (I thought I deleted it!).")
else:
    print("'footer-static-icons' container GONE.")

if 'footer-logo-grid' in html:
    print("Found 'footer-logo-grid' (Original container? at line: {})".format(html.find('footer-logo-grid')))
else:
    print("'footer-logo-grid' container GONE.")

# Check for duplicate Marquees
m_count = html.count('marquee-container')
print(f"Marquee Containers: {m_count}")
