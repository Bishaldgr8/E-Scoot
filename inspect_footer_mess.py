
# I need to see the HTML structure around the marquee to fix the "mess".
# I'll look for `marquee-container` and surrounding divs.

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('marquee-container')
if idx != -1:
    # Print 1000 chars before and after to see context (and potential duplicates)
    print(html[max(0, idx-1000):idx+2000])
else:
    print("Marquee container not found.")
