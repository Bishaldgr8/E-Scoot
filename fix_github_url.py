
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the current state of the social links
import re

# Search for the GH text to find where we changed FB to GH
gh_idx = content.find('<div class="social-txt-1">GH</div>')

if gh_idx != -1:
    print(f"Found GH at position {gh_idx}")
    
    # Look backwards for the href
    before = content[:gh_idx]
    # Find the last href before GH
    href_match = re.search(r'href="([^"]*)"[^>]*$', before[-200:])
    
    if href_match:
        current_url = href_match.group(1)
        print(f"Current GitHub URL: {current_url}")
        
        # Replace it with the correct one
        new_content = content.replace(
            f'href="{current_url}" target="_blank" class="social-icon-m',
            f'href="https://github.com/Bishaldgr8" target="_blank" class="social-icon-m'
        )
        
        with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"Updated to: https://github.com/Bishaldgr8")
    else:
        print("Could not find href pattern")
else:
    print("GH not found - searching for FB instead")
    # Maybe the FB->GH replacement didn't work, let's try again
    fb_pattern = r'<a href="https://www\.facebook\.com/[^"]*" target="_blank" class="social-icon-m w-inline-block"><div class="social-txt-1">FB</div>'
    
    if re.search(fb_pattern, content):
        print("Found FB, replacing with GitHub")
        # Replace the entire FB link with GitHub
        new_content = re.sub(
            r'(<a href=")https://www\.facebook\.com/[^"]*(" target="_blank" class="social-icon-m w-inline-block"><div class="social-txt-1">)FB(</div>)',
            r'\1https://github.com/Bishaldgr8\2GH\3',
            content
        )
        
        with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("Replaced FB with GitHub successfully")
