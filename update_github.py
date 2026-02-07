
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Update the placeholder GitHub URL with the actual one
old_github = 'href="https://github.com/yourusername"'
new_github = 'href="https://github.com/Bishaldgr8"'

content = content.replace(old_github, new_github)

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("GitHub URL updated to: https://github.com/Bishaldgr8")
