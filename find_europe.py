
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

index = 0
found = False
while True:
    index = content.find("Europe", index)
    if index == -1:
        break
    found = True
    start = max(0, index - 50)
    end = min(len(content), index + 50)
    print(f"Match at index {index}: ...{content[start:end]}...")
    index += 6

if not found:
    print("No 'Europe' found.")
