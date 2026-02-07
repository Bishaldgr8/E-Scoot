
import re

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Starting comprehensive restoration...")

# 1. Replace UJET with E SCOOT (case-sensitive replacements)
replacements = {
    'UJET': 'E SCOOT',
    'Ujet': 'E Scoot',
    'ujet': 'escoot',
}

for old, new in replacements.items():
    count = content.count(old)
    content = content.replace(old, new)
    print(f"✓ Replaced '{old}' with '{new}' ({count} occurrences)")

# 2. Update social media links
content = content.replace(
    'https://www.linkedin.com/company/ujet-int/',
    'https://www.linkedin.com/in/bishal-boro-4183a0257'
)
print("✓ Updated LinkedIn URL")

content = content.replace(
    'https://www.facebook.com/ujetofficial/',
    'https://github.com/Bishaldgr8'
)
print("✓ Replaced Facebook with GitHub")

content = content.replace('>FB<', '>GH<')
print("✓ Changed FB to GH")

# Remove Instagram
content = re.sub(
    r'<a href="https://www\.instagram\.com/[^"]*"[^>]*class="social-icon[^>]*>.*?</a>',
    '',
    content,
    flags=re.DOTALL
)
print("✓ Removed Instagram links")

# 3. Replace European/Luxembourg references with Indian
european_replacements = {
    'European': 'Indian',
    'Europe': 'India',
    'Luxembourg': 'India',
    'Luxemburg': 'India',
    'Foetz, Luxembourg': 'Room No 320, JH Hostel, IIIT UNA',
    'Ulm, Germany': 'IIIT Una, Himachal Pradesh',
}

for old, new in european_replacements.items():
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"✓ Replaced '{old}' with '{new}' ({count} occurrences)")

# 4. Update map iframe
old_map = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2610.160160160160!2d6.123456!3d49.123456'
new_map = 'https://maps.google.com/maps?q=31.481124,76.190682&t=&z=13&ie=UTF8&iwloc=&output=embed'

if old_map in content:
    content = content.replace(old_map, new_map)
    print("✓ Updated map to Indian location")
else:
    # Try to find and replace any Google Maps iframe
    content = re.sub(
        r'<iframe[^>]*src="https://www\.google\.com/maps/embed[^"]*"',
        f'<iframe src="{new_map}"',
        content
    )
    print("✓ Updated map iframe to Indian location")

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ All changes restored successfully!")
