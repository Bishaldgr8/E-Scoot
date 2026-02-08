
# Inspect what comes AFTER the swiper container to find a safe end point.

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

try:
    start = html.index('class="swiper-container"')
    # Print next 2000 chars
    print(html[start:start+2000])
except ValueError:
    print("Not found.")
