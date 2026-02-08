
# The previous output was weirdly truncated? "100%) !important; /* class"></div></a><nav cl"
# I still don't see the full context of the Marquee insertion.

# I will assume there are TWO major blocks of icons now.
# 1. The original one (which I failed to replace correctly, or which is the "Top Row").
# 2. The new Marquee (which I added).

# I will find ALL occurrences of `assets/make_in_india.svg`.
# If there are > 2 occurrences (since marquee has 2 sets), it confirms duplication of the SECTION.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = html.count('assets/make_in_india.svg')
print(f"Count of Make in India icons: {count}")

# If count > 2, we have multiple sections.
# Marquee has 2 sets (Set 1 + Duplicate). So count=2 is expected for JUST marquee.
# If count > 2 (e.g. 3), then we have Original + Marquee.

# I will also look for `class="marquee-container"`.
m_count = html.count('marquee-container')
print(f"Count of Marquee Containers: {m_count}")
