
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

start = content.find('<div class="logo-parent-w">')
if start != -1:
    print(f"Start at {start}")
    print(content[start:start+2000]) # Print enough to see all
else:
    print("logo-parent-w not found")
