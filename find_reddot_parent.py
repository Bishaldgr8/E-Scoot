
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Reddot")
if idx != -1:
    print(f"Found 'Reddot' at {idx}")
    # Print 2000 chars before
    start = max(0, idx - 2000)
    print("Preceding content:")
    print(content[start:idx])
else:
    print("Reddot not found")
