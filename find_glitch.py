
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for "Front-rank"
idx = html.find("Front-rank")
if idx != -1:
    # Print context
    print(html[max(0, idx-500):idx+500])
else:
    print("Front-rank not found")

# Also search for "We have lean and flexible"
idx2 = html.find("We have lean and flexible")
if idx2 != -1:
    print("--- Context 2 ---")
    print(html[max(0, idx2-500):idx2+500])
