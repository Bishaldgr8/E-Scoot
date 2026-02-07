
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update LinkedIn URL
content = content.replace(
    'https://www.linkedin.com/company/ujet-int/',
    'https://www.linkedin.com/in/bishal-boro-4183a0257'
)
print("✓ Updated LinkedIn URL")

# 2. Replace Facebook with GitHub
content = content.replace(
    'https://www.facebook.com/ujetofficial/',
    'https://github.com/Bishaldgr8'
)
print("✓ Replaced Facebook URL with GitHub")

# 3. Change FB text to GH
content = content.replace('>FB<', '>GH<')
print("✓ Changed FB text to GH")

# 4. Remove Instagram links entirely
import re
# Remove Instagram social icon links
content = re.sub(
    r'<a href="https://www\.instagram\.com/[^"]*"[^>]*class="social-icon[^>]*>.*?</a>',
    '',
    content,
    flags=re.DOTALL
)
print("✓ Removed Instagram links")

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ All social media updates completed successfully!")
