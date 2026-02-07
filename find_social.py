
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for common social media patterns
patterns = [
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "social",
    "footer-social",
    "icon-social"
]

for pattern in patterns:
    idx = content.lower().find(pattern.lower())
    if idx != -1:
        print(f"Found '{pattern}' at position {idx}")
        # Print context
        start = max(0, idx - 200)
        end = min(len(content), idx + 200)
        print(f"Context: {repr(content[start:end])}")
        print("\n" + "="*50 + "\n")
