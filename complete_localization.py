
import re

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Starting complete Indian localization...")

# 1. Update map iframe to IIIT Una coordinates (31.481124, 76.190682)
old_map_pattern = r'<iframe[^>]*src="https://www\.google\.com/maps/embed[^"]*"[^>]*></iframe>'
new_map = '<iframe src="https://maps.google.com/maps?q=31.481124,76.190682&t=&z=15&ie=UTF8&iwloc=&output=embed" width="100%" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>'

content = re.sub(old_map_pattern, new_map, content)
print("✓ Updated map to IIIT Una location")

# 2. Update address text
address_replacements = {
    '1 Rue de la Poudrerie': 'Room No 320, JH Hostel',
    '3364 Leudelange': 'IIIT Una',
    'Leudelange': 'IIIT Una',
    'Luxembourg': 'Himachal Pradesh, India',
    'Luxemburg': 'India',
    'Foetz, Luxembourg': 'Room No 320, JH Hostel, IIIT Una',
    'Ulm, Germany': 'IIIT Una, Himachal Pradesh',
}

for old, new in address_replacements.items():
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced '{old}' with '{new}' ({count} occurrences)")

# 3. Replace European with Indian
content = content.replace('European', 'Indian')
content = content.replace('Europe', 'India')
print("✓ Replaced European/Europe with Indian/India")

# 4. Ensure all UJET → E SCOOT replacements
ujet_replacements = {
    'UJET': 'E SCOOT',
    'Ujet': 'E Scoot',
    'ujet': 'escoot',
}

for old, new in ujet_replacements.items():
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced '{old}' with '{new}' ({count} occurrences)")

# 5. Update footer copyright
content = content.replace('Copyright © 2020 Ujet International Sarl', 'Copyright © 2026 E Scoot India')
content = content.replace('E SCOOT INTERNATIONAL SARL', 'E SCOOT INDIA')
print("✓ Updated copyright and company name")

# 6. Update email and phone (if you want to change these)
# content = content.replace('hello@ujet.com', 'hello@escoot.in')
# content = content.replace('+352 2786 34 46', '+91-XXXXXXXXXX')

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ All localization changes completed successfully!")
print("\nNote: Footer logo images still reference the original files.")
print("You'll need to replace the actual logo image files in the assets folder with Indian government logos.")
