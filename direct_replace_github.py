
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find GH position
gh_idx = content.find('<div class="social-txt-1">GH</div>')

if gh_idx != -1:
    # Get 500 chars before GH to see the full link structure
    start = max(0, gh_idx - 500)
    context = content[start:gh_idx + 100]
    
    print("Context around GH:")
    print(repr(context))
    
    # Now find the href in this context
    import re
    href_matches = re.findall(r'href="([^"]*)"', context)
    
    if href_matches:
        print(f"\nFound hrefs: {href_matches}")
        # The last href before GH should be the one we want
        current_github_url = href_matches[-1]
        print(f"Current URL: {current_github_url}")
        
        # Replace it
        content = content.replace(
            f'href="{current_github_url}"',
            f'href="https://github.com/Bishaldgr8"',
            1  # Only replace first occurrence
        )
        
        with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"\nReplaced {current_github_url} with https://github.com/Bishaldgr8")
