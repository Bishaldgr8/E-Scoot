
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

# List of old logo filenames/substrings to target
old_logos = [
    "Reddot.svg",
    "Made-in-lux.svg",
    "deutscher",
    "ny_ad_award.png",
    "adc-awards.png",
    "Designed%20in%20germany",
    "if-award.svg",
    "edison-awards.png",
    "theandys_logo.png",
    "Design In Germany"
]

def find_div_end(s, start_idx):
    count = 1
    i = start_idx + 1
    while count > 0 and i < len(s):
        if s[i:i+4] == '<div':
            count += 1
            i += 4
        elif s[i:i+6] == '</div>':
            count -= 1
            i += 6
        else:
            i += 1
    return i

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes_made = False

for logo in old_logos:
    while True:
        # Find logo
        idx = content.find(logo)
        if idx == -1:
            break
            
        print(f"Found old logo '{logo}' at {idx}")
        
        # Find start of surrounding div (logo-parent)
        # Search backwards for '<div'
        # We assume the structure matches <div class="logo-parent ...">...<img src="...logo...">...</div>
        
        # We look for the nearest '<div' before the image and check if it has "logo-parent" class?
        # Or just specific class.
        
        # Let's find '<div class="logo-parent' backwards
        
        div_start = content.rfind('<div class="logo-parent', 0, idx)
        if div_start == -1:
            print(f"Could not find parent div for {logo} (looked for '<div class=\"logo-parent')")
            # Force removal of the img tag itself if can't find div?
            # Or try just '<div'
            div_start = content.rfind('<div', 0, idx)
        
        if div_start != -1:
            div_end = find_div_end(content, div_start + 4) # +4 to get past '<div'
            
            # Sanity check: does the range include the logo?
            if idx > div_start and idx < div_end:
                print(f"Removing div at {div_start}-{div_end} containing {logo}")
                content = content[:div_start] + content[div_end:]
                changes_made = True
            else:
                print(f"Warning found div {div_start}-{div_end} but logo is at {idx} (outside). Skipping this instance.")
                # Increment search start manually to avoid infinite loop if we don't break
                # But here we are modifying content, so re-looping is fine.
                # If we fail to remove, we must break to avoid infinite loop.
                break
        else:
            print("No parent div found at all?")
            break

if changes_made:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Cleaned up old logos.")
else:
    print("No changes made.")
