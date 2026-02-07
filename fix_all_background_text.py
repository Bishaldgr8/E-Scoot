
import re

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Replacing ALL background 'Ujet' text with 'ESCO'...")

# Replace all instances of the large background letters
# Pattern 1: lg-slide-txt (main background letters)
replacements = [
    ('lg-slide-txt one">U ', 'lg-slide-txt one">E '),
    ('lg-slide-txt two">j ', 'lg-slide-txt two">S '),
    ('lg-slide-txt three">e ', 'lg-slide-txt three">C '),
    ('lg-slide-txt four">t ', 'lg-slide-txt four">O '),
]

for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced {count} instance(s) of '{old}' with '{new}'")

# Pattern 2: lg-slide-txt light-lg (another variation)
light_replacements = [
    ('lg-slide-txt light-lg one">U ', 'lg-slide-txt light-lg one">E '),
    ('lg-slide-txt light-lg two">j ', 'lg-slide-txt light-lg two">S '),
    ('lg-slide-txt light-lg three">e ', 'lg-slide-txt light-lg three">C '),
    ('lg-slide-txt light-lg four">t ', 'lg-slide-txt light-lg four">O '),
]

for old, new in light_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced {count} instance(s) of '{old}' with '{new}'")

# Pattern 3: Mobile menu darker version (already done but double-check)
mobile_replacements = [
    ('lg-slide-txt-darker one">U ', 'lg-slide-txt-darker one">E '),
    ('lg-slide-txt-darker two">j ', 'lg-slide-txt-darker two">S '),
    ('lg-slide-txt-darker three">e ', 'lg-slide-txt-darker three">C '),
    ('lg-slide-txt-darker four">t ', 'lg-slide-txt-darker four">O '),
]

for old, new in mobile_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced {count} instance(s) of '{old}' with '{new}'")

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ All background text updated from 'Ujet' to 'ESCO'!")
print("Please refresh http://localhost:8000 to see the changes.")
