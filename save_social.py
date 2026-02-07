
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

output = []

# Search for social media links
patterns = ["linkedin.com", "facebook.com", "instagram.com", "twitter.com"]

for pattern in patterns:
    idx = content.lower().find(pattern.lower())
    if idx != -1:
        output.append(f"Found '{pattern}' at position {idx}\n")
        # Print larger context
        start = max(0, idx - 300)
        end = min(len(content), idx + 300)
        output.append(f"Context:\n{content[start:end]}\n")
        output.append("\n" + "="*80 + "\n\n")

with open(r"c:\Users\assdr\Desktop\New Project\social_links.txt", "w", encoding="utf-8") as f:
    f.write("".join(output))

print("Social media links saved to social_links.txt")
