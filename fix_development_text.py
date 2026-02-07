
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the text
idx = content.find("DEVELOPMENT")
if idx != -1:
    # Look for the h3 tag containing it
    # Search backwards for <h3
    start_search = max(0, idx - 500)
    before = content[start_search:idx]
    
    h3_start = before.rfind('<h3')
    if h3_start != -1:
        abs_h3_start = start_search + h3_start
        
        # Find the closing </h3>
        after = content[idx:]
        h3_end = after.find('</h3>')
        
        if h3_end != -1:
            abs_h3_end = idx + h3_end + 5  # +5 for </h3>
            
            # Extract the full h3 element
            h3_element = content[abs_h3_start:abs_h3_end]
            
            print("Original h3 element:")
            print(h3_element)
            
            # Remove any <br/> or <br> tags from within this h3
            fixed_h3 = h3_element.replace('<br/>', ' ').replace('<br>', ' ')
            
            # Also ensure proper spacing
            import re
            fixed_h3 = re.sub(r'\s+', ' ', fixed_h3)
            
            print("\nFixed h3 element:")
            print(fixed_h3)
            
            # Replace in content
            new_content = content[:abs_h3_start] + fixed_h3 + content[abs_h3_end:]
            
            with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
                f.write(new_content)
            
            print("\nReplacement successful!")
        else:
            print("Could not find closing </h3>")
    else:
        print("Could not find opening <h3")
else:
    print("DEVELOPMENT not found")
