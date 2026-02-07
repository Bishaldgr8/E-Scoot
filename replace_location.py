
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace "European" -> "Indian"
# Use regex to ensure word boundaries if possible, but simpler string replacement might suffice given HTML content
new_content = content.replace("European", "Indian")

# Replace "Europe" -> "India"
# Be careful not to replace "Indian" -> "Indiapan" or similar if "Europe" was part of it
# But since we replaced "European" first, "Europe" remaining should be standalone or suffix?
# "Indian" does not contain "Europe".
# So replacing "Europe" -> "India" should be safe for "European" instances that became "Indian".
# However, if there are other words containing "Europe", e.g. "European" (already handled), "Indo-European" -> "Indo-Indian".
# I'll replace "Europe" with "India".
new_content = new_content.replace("Europe", "India")

# Replace "Luxembourg" -> "India"
new_content = new_content.replace("Luxembourg", "India")
new_content = new_content.replace("Luxemburg", "India")

# Check if changes were made
if content != new_content:
    print("Replaced content.")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
else:
    print("No changes made.")
