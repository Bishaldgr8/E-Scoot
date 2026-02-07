import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Center the footer attribution text
# Find the footer-child div and update it to center the content
old_footer_pattern = r'<div class="footer-txt-sm" style="display: flex; align-items: center; gap: 15px;">[\s\S]*?</div>'
new_footer = '''<div class="footer-txt-sm" style="display: flex; align-items: center; justify-content: center; gap: 15px;">
        <img src="assets/5f3f94975bc16034133c0c47_E Scoot-logo-light.svg" width="80" alt="E Scoot Logo" style="filter: brightness(0.8);"/>
        <span>Made with precision by BISHAL B</span>
      </div>'''

html = re.sub(old_footer_pattern, new_footer, html)

# 2. Update the address in the map section
# Replace "1, Rue de la Poudrerie" with "Room No 320, JH Hostel,"
old_address = r'1, Rue de la Poudrerie<br/>IIIT Una<br/>India'
new_address = 'Room No 320, JH Hostel,<br/>IIIT Una,<br/>India'

html = html.replace(old_address, new_address)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Footer attribution centered")
print("✓ Address updated to: Room No 320, JH Hostel, IIIT Una, India")
