
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Reddot")
if idx != -1:
    print(f"Found 'Reddot' at {idx}")
    # Print 500 chars before and after
    start = max(0, idx - 500)
    end = min(len(content), idx + 500)
    print(content[start:end])
else:
    print("Reddot not found")
