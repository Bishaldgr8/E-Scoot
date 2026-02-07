import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's add a more robust centering solution using CSS
# Find the footer section and add width: 100% to ensure it spans the full width
old_footer_txt = r'<div class="footer-txt-sm"[^>]*>[\s\S]*?</div>'
new_footer_txt = '''<div class="footer-txt-sm" style="display: flex; align-items: center; justify-content: center; gap: 15px; width: 100%; text-align: center;">
        <img src="assets/5f3f94975bc16034133c0c47_E Scoot-logo-light.svg" width="80" alt="E Scoot Logo" style="filter: brightness(0.8);"/>
        <span>Made with precision by BISHAL B</span>
      </div>'''

html = re.sub(old_footer_txt, new_footer_txt, html)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ Footer now uses full width with flex centering")
print("✓ Text should be perfectly centered")
