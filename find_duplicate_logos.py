
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("logo-marquee")
if idx != -1:
    # Look at 3000 chars before
    start = max(0, idx - 3000)
    preceding = content[start:idx]
    
    # Find all img tags in preceding
    import re
    imgs = re.findall(r'<img[^>]+>', preceding)
    if imgs:
        print(f"Found {len(imgs)} images before marquee.")
        for img in imgs[-5:]: # Show last 5
            print(img)
            
        # Also print the last 500 characters of preceding to see immediate context
        print("\nImmediate context before marquee:")
        print(repr(preceding[-500:]))
    else:
        print("No images found in the 3000 chars before marquee.")
else:
    print("logo-marquee not found")
