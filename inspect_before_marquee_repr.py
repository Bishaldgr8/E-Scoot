
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("logo-marquee")
if idx != -1:
    # Print 2000 chars before
    start = max(0, idx - 2000)
    print(repr(content[start:idx]))
else:
    print("logo-marquee not found")
