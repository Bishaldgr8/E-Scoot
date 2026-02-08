
# 4th Member disappeared.
# Delete "Made in Webflow".

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Delete Webflow Badge.
# Often checks for `w-webflow-badge` class.
if 'w-webflow-badge' in html:
    # Regex to remove the entire element.
    # <a ... class="... w-webflow-badge ...">...</a>
    # It usually is at the end of body.
    html = re.sub(r'<a[^>]*class="[^"]*w-webflow-badge[^"]*"[^>]*>.*?</a>', '', html, flags=re.DOTALL)
    print("Removed Webflow badge.")
else:
    print("Webflow badge class not found. Searching for generic webflow text.")

# 2. Check 4th Member Visibility.
# Rapunzal S.
# Ensure Swiper allows enough space or loop?
# In Step 2917, `slidesOffsetAfter: 310` was set.
# If `slidesPerView: 'auto'`, and width is fixed 279px.
# Maybe `slidesOffsetAfter` is pushing it out?
# Or maybe the container width is cut off?

# I will try to make the specific slide visible by ensuring no `display: none`.
# But Swiper logic is JS.
# I'll check if I broke the HTML.
# Count `swiper-slide` divs.

c = html.count('class="swiper-slide"')
print(f"Number of slides found: {c}")
# Should be 4.

# Maybe the USER removed it? Or I did?
# "fourth member disappeared" -> User implies it happened after my changes.
# I haven't deleted slides.
# I'll check if Rapunzal is in the HTML.
if 'Rapunzal S' in html:
    print("Rapunzal S is present in HTML.")
else:
    print("WARNING: Rapunzal S is MISSING from HTML.")

# I'll also add CSS to hide the badge if I couldn't find the tag.
css_hide_badge = '''
<style>
.w-webflow-badge { display: none !important; }
</style>
'''
html = html.replace('</head>', css_hide_badge + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
