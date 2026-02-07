
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for DEVELOPMENT
idx = content.find("DEVELOPMENT")
if idx != -1:
    print(f"Found 'DEVELOPMENT' at {idx}")
    # Print surrounding context
    start = max(0, idx - 300)
    end = min(len(content), idx + 300)
    print("\nContext:")
    print(repr(content[start:end]))
else:
    print("DEVELOPMENT not found")
    
# Also search for case studies
idx2 = content.lower().find("case studies")
if idx2 != -1:
    print(f"\nFound 'case studies' at {idx2}")
    start = max(0, idx2 - 300)
    end = min(len(content), idx2 + 300)
    print("\nContext:")
    print(repr(content[start:end]))
