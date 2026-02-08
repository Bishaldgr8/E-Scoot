
# Validating context from previous output:
# --- Context for Arnpre ---
# ... v><y Officer</div></div
# (base)le="width:0%" cl

# The output was truncated and useless.
# I need to see the start of the `name` div.
# I'll search for `Arnpreet` and print 50 chars BEFORE it.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

names = ["Arnpreet Y", "Rapunzal S"]
for name in names:
    idx = html.find(name)
    if idx != -1:
        print(f"--- Context for {name} ---")
        print(html[max(0, idx-50):idx+20])
