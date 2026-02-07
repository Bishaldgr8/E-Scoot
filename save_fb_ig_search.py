
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

output_lines = []

# Find all FB
fb_positions = []
idx = 0
while True:
    idx = content.find('>FB<', idx)
    if idx == -1:
        break
    fb_positions.append(idx)
    idx += 1

# Find all IG  
ig_positions = []
idx = 0
while True:
    idx = content.find('>IG<', idx)
    if idx == -1:
        break
    ig_positions.append(idx)
    idx += 1

output_lines.append(f"Found {len(fb_positions)} instances of '>FB<'\n")
for i, pos in enumerate(fb_positions, 1):
    start = max(0, pos - 300)
    end = min(len(content), pos + 300)
    output_lines.append(f"\n{i}. Position {pos}:\n")
    output_lines.append(f"Context:\n{content[start:end]}\n")
    output_lines.append("="*80 + "\n")

output_lines.append(f"\n\nFound {len(ig_positions)} instances of '>IG<'\n")
for i, pos in enumerate(ig_positions, 1):
    start = max(0, pos - 300)
    end = min(len(content), pos + 300)
    output_lines.append(f"\n{i}. Position {pos}:\n")
    output_lines.append(f"Context:\n{content[start:end]}\n")
    output_lines.append("="*80 + "\n")

with open(r"c:\Users\assdr\Desktop\New Project\fb_ig_results.txt", "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print(f"Results saved. FB: {len(fb_positions)}, IG: {len(ig_positions)}")
