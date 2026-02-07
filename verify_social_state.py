
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for all social media related patterns
import re

# Find all social-icon-m links
social_links = re.findall(r'<a href="([^"]*)" target="_blank" class="social-icon-m[^>]*>.*?<div class="social-txt-1">([^<]*)</div>', content, re.DOTALL)

print("Current social links:")
for url, text in social_links:
    print(f"  {text}: {url}")

# Also check if facebook.com still exists
if 'facebook.com' in content:
    print("\nFacebook URL still exists in the file!")
    fb_idx = content.find('facebook.com')
    print(f"At position: {fb_idx}")
    print(f"Context: {repr(content[fb_idx-50:fb_idx+100])}")
