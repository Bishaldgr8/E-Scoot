import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update footer: add margin-top to push logo down, ensure text is centered
old_footer_txt = r'<div class="footer-txt-sm"[^>]*>[\s\S]*?</div>'
new_footer_txt = '''<div class="footer-txt-sm" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; width: 100%; text-align: center; margin-top: 20px;">
        <img src="assets/5f3f94975bc16034133c0c47_E Scoot-logo-light.svg" width="100" alt="E Scoot Logo" style="filter: brightness(0.8); display: block;"/>
        <span style="display: block; width: 100%; text-align: center;">Made with precision by BISHAL B</span>
      </div>'''

html = re.sub(old_footer_txt, new_footer_txt, html)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Logo moved down with margin-top: 20px")
print("✓ Text centered relative to logo with width: 100%")
