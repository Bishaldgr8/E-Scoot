
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find all social-txt-1 divs
import re
social_texts = re.findall(r'<div class="social-txt-1">([^<]*)</div>', content)

print("Current social icon texts:")
for i, text in enumerate(social_texts, 1):
    print(f"  {i}. {text}")

# Count occurrences
print(f"\nTotal social icons: {len(social_texts)}")
print(f"FB count: {social_texts.count('FB')}")
print(f"GH count: {social_texts.count('GH')}")
print(f"IG count: {social_texts.count('IG')}")
print(f"IN count: {social_texts.count('IN')}")
