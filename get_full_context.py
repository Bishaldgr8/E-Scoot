
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find DEVELOPMENT
idx = content.find("DEVELOPMENT")
if idx != -1:
    # Get 1500 chars before and after to see full structure
    start = max(0, idx - 1500)
    end = min(len(content), idx + 500)
    
    section = content[start:end]
    
    # Pretty print with line breaks at tags
    import re
    formatted = re.sub(r'(<[^>]+>)', r'\n\1\n', section)
    
    print(formatted)
else:
    print("Not found")
