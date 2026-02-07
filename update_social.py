
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update LinkedIn URL
old_linkedin = 'https://www.linkedin.com/company/ujet-int/'
new_linkedin = 'https://www.linkedin.com/in/bishal-boro-4183a0257'
content = content.replace(old_linkedin, new_linkedin)
print(f"Updated LinkedIn URL")

# 2. Replace Facebook with GitHub
# Find the Facebook link and replace it with GitHub
old_fb = 'href="https://www.facebook.com/ujetofficial/"'
new_github = 'href="https://github.com/yourusername"'  # User will need to provide their GitHub username

# Also change the text from FB to GH (for GitHub)
content = content.replace(old_fb, new_github)
content = content.replace('<div class="social-txt-1">FB</div>', '<div class="social-txt-1">GH</div>')
print(f"Replaced Facebook with GitHub")

# 3. Remove Instagram link entirely
# Find and remove the entire Instagram anchor tag
import re
# Pattern to match the Instagram link
ig_pattern = r'<a href="https://www\.instagram\.com/[^"]*" target="_blank" class="social-icon-m w-inline-block">.*?</a>'
content = re.sub(ig_pattern, '', content, flags=re.DOTALL)
print(f"Removed Instagram link")

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\nAll social media updates completed!")
