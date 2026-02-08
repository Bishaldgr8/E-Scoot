
# Check if inline styles exist in index.html.

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = html.count('style="width: 22% !important; margin-right: 2% !important;"')
print(f"Found {count} patched swiper-slides.")

if count == 0:
    print("Patch NOT found! Something went wrong.")
    # Print a snippet of what a swiper slide looks like
    import re
    m = re.search(r'<div[^>]*swiper-slide[^>]*>', html)
    if m:
        print("Sample tag:", m.group(0))
