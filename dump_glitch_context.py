
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Search for "Front-rank"
idx = html.find("Front-rank")
if idx != -1:
    # Save 2000 chars of context
    context = html[max(0, idx-1000):idx+1000]
    with open('glitch_context.txt', 'w', encoding='utf-8') as f:
        f.write(context)
    print("Context saved to glitch_context.txt")
else:
    print("Front-rank not found")
