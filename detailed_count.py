
# Validating if `footer-logo-grid` doesn't exist but `Make In India` check returned 12.
# 12 is EXACTLY 6 * 2 (one marquee set duplicated).
# This implies there IS ONLY ONE MARQUEE belt?
# And NO OTHER ICONS of "Make In India".

# So why does the user say "it is still there"?
# "It" = Wait.
# Look at Step 2809 Screenshot.
# Bottom: Marquee.
# Top: White space.
# Is "it" the Marquee ITSELF?
# "it is still there. im fed up" -> "The BELT is still there".
# Does the user HATE THE MARQUEE?
# But they asked: "move them in a line endlessly".
# Maybe they check Step 2745: "delete these" (Static one). "delete the static ones and move them in a line endlessly".

# Maybe the user sees TWO marquees?
# If `count` says 12, then I have ONE marquee (with 6 unique items doubled).
# Is it possible valid marquee has 12 items, but displayed twice on screen visually due to CSS?
# Or maybe I have another set of images that are NOT `make_in_india.svg`?
# e.g. `iiit_una_logo.png`?

# Let's count ALL images to be sure.
# And compare to 12.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Count all img tags in body?
# Or just scan for footer assets.
assets = ['make_in_india.svg', 'iiit_una_logo.png', 'govt_of_india.png', 'digital_india.svg', 'swachh_bharat.svg', 'made_in_india.svg']

for asset in assets:
    c = html.count(f'assets/{asset}')
    print(f"{asset}: {c}")

# Also check for `marquee-container` count again.
m_count = html.count('marquee-container')
print(f"Marquee Containers: {m_count}")
