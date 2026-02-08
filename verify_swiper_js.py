
# Verify JS config is correct for CSS-driven width.
# Expect: `slidesPerView: 'auto'` (or similar).

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if "slidesPerView: 'auto'" in html:
    print("JS config is correct: slidesPerView: 'auto'")
elif "slidesPerView: 4" in html:
    print("JS config is: slidesPerView: 4 (This might conflict if CSS is used)")
else:
    print("JS config not found or different.")
