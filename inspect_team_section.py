
# Reading index.html to find the Team Section bounds.
# I'll look for "swiper-container" and surrounding tags.
# Also "Meet the Team" or similar headers.

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the context around the swiper.
try:
    start_idx = html.index('class="swiper-container"')
    # Show 500 chars before and 1000 chars after to see the wrapper.
    snippet = html[max(0, start_idx-500):min(len(html), start_idx+3000)]
    print("--- Context Snippet ---")
    print(snippet)
except ValueError:
    print("Could not find 'class=\"swiper-container\"' in index.html (Did I delete it??)")
