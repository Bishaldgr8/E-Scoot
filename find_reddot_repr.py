
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Reddot")
if idx != -1:
    # Print 500 chars before
    start = max(0, idx - 500)
    print(repr(content[start:idx]))
else:
    print("Reddot not found")
