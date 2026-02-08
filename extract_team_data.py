
# Extract team member details from index.html before deleting.
# Need Name, Role, Image Source, Quote.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Regex to find slide content.
# Patterns:
# Image: <img src="(...)" ...>
# Name: <h4 ...>(...)</h4>
# Role: <div class="job-title|designation|...">(...)</div>
# Quote: <div class="team-quote">(...)</div>

slides = re.findall(r'<div[^>]*class="[^"]*swiper-slide[^"]*"[^>]*>(.*?)</div>\s*<!--', html, re.DOTALL)
# The slide div closes. But regex ".*?" might stop early or eat too much if nested divs exist.
# Better to find `swiper-slide` start, then parse inside.
# But simply finding names/quotes globaly might work if order is preserved.

print("--- Extracting Data ---")

names = re.findall(r'<h4[^>]*class="[^"]*name[^"]*"[^>]*>(.*?)</h4>', html)
roles = re.findall(r'<div[^>]*class="[^"]*job-title[^"]*"[^>]*>(.*?)</div>', html) # Class might be `job-title` or `designation`
quotes = re.findall(r'<div[^>]*class="[^"]*team-quote[^"]*"[^>]*>(.*?)</div>', html)
images = re.findall(r'<img[^>]*src="([^"]*)"[^>]*class="[^"]*team-image[^"]*"', html) # Class might differ

print(f"Names ({len(names)}): {names}")
print(f"Roles ({len(roles)}): {roles}")
print(f"Quotes ({len(quotes)}): {quotes}")
print(f"Images ({len(images)}): {images}")

# Adjust regex if empty.
if not names:
    # Try generic h4
    names = re.findall(r'<h4[^>]*>(.*?)</h4>', html)
    # Filter for known names?
    
if not roles:
    # Try class `designation` (from previous turns)
    roles = re.findall(r'<div[^>]*class="[^"]*designation[^"]*"[^>]*>(.*?)</div>', html)

# If images fail, look for any image inside swiper-slide.
