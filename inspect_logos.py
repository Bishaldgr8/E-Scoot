
with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="logo-parent-w">'
# Find all occurrences
indices = []
idx = 0
while True:
    idx = content.find(start_marker, idx)
    if idx == -1:
        break
    indices.append(idx)
    idx += 1

print(f"Found {len(indices)} occurrences of logo-parent-w.")

for i, idx in enumerate(indices):
    print(f"\n--- Occurrence {i+1} at index {idx} ---")
    # Print 500 chars after
    print(content[idx:idx+1000])
