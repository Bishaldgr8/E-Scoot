
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="logo-parent-w">'
end_marker = '</div></div><div class="footer-parent">' 
# Finding the end might be tricky if it's nested.
# Let's find the start and print some characters.

idx = content.find(start_marker)
if idx != -1:
    print(f"Found at {idx}")
    print(content[idx:idx+1000]) # Print enough to see the structure
else:
    print("Not found")
