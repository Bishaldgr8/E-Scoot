
import re

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Updating footer logos to Indian government logos...")

# Find the footer logo section and replace it
# The logos are in <div class="logo-parent-w"> sections

# Define the new logo HTML structure
new_logos = '''<div class="logo-parent pr-60 width-240"><img src="assets/made_in_india.svg" width="100" alt="Made In India"/></div><div class="logo-parent pr-60 width-240"><img src="assets/iiit_una_logo.png" width="120" alt="IIIT Una"/></div><div class="logo-parent pr-60 width-240"><img src="assets/govt_of_india.png" width="80" alt="Government of India"/></div><div class="logo-parent pr-60 width-240"><img src="assets/digital_india.svg" width="140" alt="Digital India"/></div><div class="logo-parent pr-60 width-240"><img src="assets/make_in_india.svg" width="120" alt="Make In India"/></div><div class="logo-parent pr-60 width-240"><img src="assets/swachh_bharat.svg" width="100" alt="Swachh Bharat"/></div>'''

# Pattern to match the logo-parent-w div content (all logos between the opening and closing div tags)
pattern = r'(<div class="logo-parent-w">)(.*?)(</div>\s*<div class="logo-parent-w">)(.*?)(</div>)'

# Find all logo sections
logo_sections = re.findall(r'<div class="logo-parent-w">(.*?)</div>\s*(?=<div class="logo-parent-w">|<div class="footer-parent">)', content, re.DOTALL)

if logo_sections:
    # Replace both logo-parent-w sections (there are two identical ones for the marquee effect)
    # First, find the entire footer section
    footer_start = content.find('<div class="container-ptb-60">')
    footer_end = content.find('<div class="footer-parent">', footer_start)
    
    if footer_start != -1 and footer_end != -1:
        # Replace the entire logo section
        new_footer_logos = f'''<div class="container-ptb-60"><div class="logo-parent-w">{new_logos}</div><div class="logo-parent-w">{new_logos}</div></div>'''
        
        # Find and replace
        old_section = content[footer_start:footer_end]
        content = content.replace(old_section, new_footer_logos)
        
        print("✓ Updated footer logos successfully!")
        print(f"  - Made in India")
        print(f"  - IIIT Una Logo")
        print(f"  - Government of India")
        print(f"  - Digital India")
        print(f"  - Make in India")
        print(f"  - Swachh Bharat")
    else:
        print("⚠ Could not find footer section")
else:
    print("⚠ Could not find logo sections")

with open(r"c:\Users\assdr\Desktop\New Project\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ Footer logos updated successfully!")
