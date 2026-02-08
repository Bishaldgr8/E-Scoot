
# Validating if `footer-logo-grid` exists and contains icons.
# Ensuring I remove the "Original Belt".

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'footer-logo-grid' in html:
    print("Found 'footer-logo-grid'. Checking content...")
    start = html.find('footer-logo-grid')
    print(html[max(0, start-100):start+1000])
else:
    print("'footer-logo-grid' not found.")

# Also check for any other image sequences that match the logos.
# make_in_india.svg seems to be the key.
count = html.count('assets/make_in_india.svg')
print(f"Total Make In India icons: {count}")
# Marquee has 12. If > 12, we have the ghost belt.
