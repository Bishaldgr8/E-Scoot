
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
            
            with open(r"c:\Users\assdr\Desktop\New Project\h3_debug.txt", "w", encoding="utf-8") as out:
                out.write("Full h3 element:\n")
                out.write(repr(h3_element))
                out.write("\n\n")
                out.write("Actual h3 element:\n")
                out.write(h3_element)
            
            print("Debug info written to h3_debug.txt")
