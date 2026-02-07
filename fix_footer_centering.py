import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the footer-child section and update it to center everything
# We need to add text-align: center to the parent div
old_pattern = r'<div class="footer-child">'
new_pattern = '<div class="footer-child" style="text-align: center;">'

html = html.replace(old_pattern, new_pattern)

# Also ensure the footer-txt-sm div itself is centered
old_footer_txt = r'<div class="footer-txt-sm"[^>]*>[\s\S]*?</div>'
new_footer_txt = '''<div class="footer-txt-sm" style="display: inline-flex; align-items: center; justify-content: center; gap: 15px; margin: 0 auto;">
        <img src="assets/5f3f94975bc16034133c0c47_E Scoot-logo-light.svg" width="80" alt="E Scoot Logo" style="filter: brightness(0.8);"/>
        <span>Made with precision by BISHAL B</span>
      </div>'''

html = re.sub(old_footer_txt, new_footer_txt, html)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Footer attribution properly centered")
print("✓ Applied text-align: center to parent container")
print("✓ Changed display to inline-flex with margin auto")
