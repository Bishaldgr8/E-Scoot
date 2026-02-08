
# Previous script failed (syntax error?).
# Rewriting `inspect_footer.py` carefully.

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('assets/make_in_india.svg')
if idx != -1:
    print(html[idx-200:idx+600])
else:
    print("Not found")
