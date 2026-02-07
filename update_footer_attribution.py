import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace the copyright text with logo and custom attribution
# Looking for the footer-txt-sm div with copyright text
old_copyright = r'<div class="footer-txt-sm">Copyright © 2020 E Scoot International Sarl\. All Rights Reserved</div>'
new_footer = '''<div class="footer-txt-sm" style="display: flex; align-items: center; gap: 15px;">
        <img src="assets/5f3f94975bc16034133c0c47_E Scoot-logo-light.svg" width="80" alt="E Scoot Logo" style="filter: brightness(0.8);"/>
        <span>Made with precision by BISHAL B</span>
      </div>'''

# Replace the copyright
html = re.sub(old_copyright, new_footer, html)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Footer updated successfully!")
print("- Added E Scoot logo")
print("- Changed copyright to 'Made with precision by BISHAL B'")
