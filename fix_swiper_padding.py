
# 4th member exists but is hidden.
# Likely `slidesOffsetAfter: 310`.
# 310px is huge. If container is small, it pushes the last slide out.
# I will REMOVE `slidesOffsetAfter`.
# Also check `margin-right` on slides (30px).

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Swiper Config.
# Look for `slidesOffsetAfter: 310`.
if 'slidesOffsetAfter' in html:
    html = re.sub(r'slidesOffsetAfter:\s*\d+,?', '', html)
    print("Removed slidesOffsetAfter.")

# Also remove Webflow badge if previous script missed it (it searched for class, maybe it's an ID or just text?).
# I'll add a CSS rule to be sure: `.w-webflow-badge {display:none !important;}` wsa added.
# I'll also try to find the element by text content if class is missing.
# But CSS hiding is usually enough.

# Adjust slide margin?
# `.swiper-slide { ... margin-right: 30px !important; }`
# If we have 4 slides * 279px + 3 * 30px = 1116px + 90 = 1206px.
# If container is smaller, `slidesPerView: 'auto'` works but scrolling is needed.
# If `slidesOffsetAfter` was adding 310px padding at the end, users might not scroll far enough?
# Or it pushed it off canvas?

# Let's see if there's `slidesOffsetBefore`.
# No.

# I'll save the file with `slidesOffsetAfter` removed.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
