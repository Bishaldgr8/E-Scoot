
# Validating regex failure. I will print the HTML around the names.
names = ["Arnpreet Y", "Rapunzal S", "Bishal B", "Ambatokandh Singh"]

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for name in names:
    idx = html.find(name)
    if idx != -1:
        print(f"--- Context for {name} ---")
        print(html[max(0, idx-100):idx+100])
    else:
        print(f"Could not find {name} in HTML.")
