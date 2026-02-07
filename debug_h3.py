
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find DEVELOPMENT
idx = content.find("DEVELOPMENT")
if idx != -1:
    # Get the h3 element
    start_search = max(0, idx - 500)
    before = content[start_search:idx]
    
    h3_start = before.rfind('<h3')
    if h3_start != -1:
        abs_h3_start = start_search + h3_start
        
        # Find closing
        after = content[idx:]
        h3_end = after.find('</h3>')
        
        if h3_end != -1:
            abs_h3_end = idx + h3_end + 5
            
            h3_element = content[abs_h3_start:abs_h3_end]
            
            print("Full h3 element:")
            print(repr(h3_element))
            print("\n\nLength:", len(h3_element))
            
            # Check for any special characters or tags
            import re
            tags = re.findall(r'<[^>]+>', h3_element)
            print("\nTags found:", tags)
            
            # Get just the text content
            text_only = re.sub(r'<[^>]+>', '', h3_element)
            print("\nText only:", repr(text_only))
