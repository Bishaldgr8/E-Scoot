
import re
from html.parser import HTMLParser

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the DEVELOPMENT text
idx = content.find("DEVELOPMENT")
if idx != -1:
    # Extract a larger chunk around it
    start = max(0, idx - 1000)
    end = min(len(content), idx + 1000)
    chunk = content[start:end]
    
    # Try to find the containing element
    # Look backwards for opening tags
    before = content[start:idx]
    
    # Find the last opening h1, h2, h3, div, etc before DEVELOPMENT
    tags = ['<h1', '<h2', '<h3', '<div', '<p']
    last_tag_pos = -1
    last_tag = None
    
    for tag in tags:
        pos = before.rfind(tag)
        if pos > last_tag_pos:
            last_tag_pos = pos
            last_tag = tag
    
    if last_tag_pos != -1:
        # Extract from that tag
        abs_start = start + last_tag_pos
        # Find the closing tag
        tag_name = last_tag.strip('<')
        closing_tag = f'</{tag_name}>'
        
        # Search forward for closing
        after_dev = content[idx:]
        close_pos = after_dev.find(closing_tag)
        
        if close_pos != -1:
            abs_end = idx + close_pos + len(closing_tag)
            element = content[abs_start:abs_end]
            
            print(f"Found element from {abs_start} to {abs_end}")
            print(f"Tag: {last_tag}")
            print("\nElement content:")
            print(element[:500])  # Print first 500 chars
            
            # Check for class attributes
            class_match = re.search(r'class="([^"]*)"', element[:200])
            if class_match:
                print(f"\nClass: {class_match.group(1)}")
        else:
            print(f"Could not find closing tag for {last_tag}")
    else:
        print("Could not find containing tag")
        print("\nRaw context:")
        print(chunk)
else:
    print("DEVELOPMENT not found")
