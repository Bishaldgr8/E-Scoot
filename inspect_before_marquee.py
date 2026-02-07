
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("logo-marquee")
if idx != -1:
    print(f"Found 'logo-marquee' at {idx}")
    # Print 2000 chars before to see what's above it
    start = max(0, idx - 2000)
    print("Preceding content:")
    print(content[start:idx])
else:
    print("logo-marquee not found")
