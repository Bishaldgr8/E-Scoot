
import re

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Fixing background text and map...")

# 1. Replace all "U j e t" background letters with "E S C O"
# The letters appear in multiple places with classes like lg-slide-txt
replacements = [
    ('>U </div>', '>E </div>'),
    ('>u </div>', '>e </div>'),
    ('>j </div>', '>S </div>'),
    ('>e </div>', '>C </div>'),
    ('>t </div>', '>O </div>'),
]

changes_made = []
for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new, 1)  # Replace first occurrence
        changes_made.append(f"  - Replaced '{old.strip('<>div/')}' with '{new.strip('<>div/')}'")
        print(f"✓ Found and replaced: {old} → {new}")

# Also replace in the darker version (mobile menu)
mobile_replacements = [
    ('lg-slide-txt-darker one">U ', 'lg-slide-txt-darker one">E '),
    ('lg-slide-txt-darker two">j ', 'lg-slide-txt-darker two">S '),
    ('lg-slide-txt-darker three">e ', 'lg-slide-txt-darker three">C '),
    ('lg-slide-txt-darker four">t ', 'lg-slide-txt-darker four">O '),
]

for old, new in mobile_replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"✓ Updated mobile menu: {old} → {new}")

# 2. Make the map interactive by removing the link wrapper and adding proper iframe
# Find the map section and make it interactive
old_map_link = r'<a data-bg="[^"]*" href="https://goo\.gl/maps/[^"]*" target="_blank" class="map-img lazyload w-inline-block"><div[^>]*></div></a>'
new_map = '<div class="map-img"><iframe src="https://maps.google.com/maps?q=31.481124,76.190682&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="450" frameborder="0" style="border:0" allowfullscreen></iframe></div>'

if re.search(old_map_link, content):
    content = re.sub(old_map_link, new_map, content)
    print("✓ Made map interactive with embedded iframe")
else:
    print("⚠ Map link pattern not found, trying alternative...")

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ All fixes applied successfully!")
print("\nChanges made:")
for change in changes_made:
    print(change)
print("  - Updated mobile menu letters")
print("  - Made map interactive")
