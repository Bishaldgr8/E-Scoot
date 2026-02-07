
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for FB and IG anywhere in the file
fb_positions = []
ig_positions = []

# Find all FB
idx = 0
while True:
    idx = content.find('>FB<', idx)
    if idx == -1:
        break
    fb_positions.append(idx)
    idx += 1

# Find all IG  
idx = 0
while True:
    idx = content.find('>IG<', idx)
    if idx == -1:
        break
    ig_positions.append(idx)
    idx += 1

print(f"Found {len(fb_positions)} instances of '>FB<'")
for i, pos in enumerate(fb_positions, 1):
    start = max(0, pos - 150)
    end = min(len(content), pos + 150)
    print(f"\n{i}. Position {pos}:")
    print(f"Context: {repr(content[start:end])}")

print(f"\n\nFound {len(ig_positions)} instances of '>IG<'")
for i, pos in enumerate(ig_positions, 1):
    start = max(0, pos - 150)
    end = min(len(content), pos + 150)
    print(f"\n{i}. Position {pos}:")
    print(f"Context: {repr(content[start:end])}")
