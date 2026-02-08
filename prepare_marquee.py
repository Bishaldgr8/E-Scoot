
# The previous output was truncated again.
# "alt='Government of Ind... width-24-parent pr-60"
# This suggests there is a container `width-24-parent pr-60`?
# Or maybe `pr-60` is a class.

# I will replace the ENTIRE block that contains these images.
# I'll search for the first image and the last image?
# Or just reconstruct the whole footer logo section.

# Let's find the start index of `class="footer-logo-grid"` or similar?
# I'll try to find the container div.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will look for the image tags and their immediate parent.
# START: <img src="assets/make_in_india.svg"
# END: <img src="assets/swachh_bharat.svg" (or whichever is last)

# Actually, the user wants REPLACEMENT.
# So I will find the block containing these images.
# I'll use a regex to find the `<div>` wrapper.

# Strategy:
# Find `assets/make_in_india.svg`.
# Find the `Set of images`.
# Replace the whole block with `<div class="marquee-container">...</div>`.

# Regex for the block of images:
# (?:<img[^>]*src="assets/[^"]*"[^>]*>\s*)+
# Wrapped in a div?

# Let's simple search for a Chunk of text I saw in Step 2661.
# "width-24-parent pr-60"
# If I find this, I can replace the parent/sibling structure.

# But simpler:
# I will just find the `assets/make_in_india.svg` and traverse up to the container.
# Or better: I will replace the Known Content.

known_content_snippet = 'assets/make_in_india.svg'
idx = html.find(known_content_snippet)
if idx != -1:
    # Find the start of the line or the parent div
    # I'll assume it's inside a `div` and I want to replace that `div`.
    # Let's find the `> <` boundaries.
    
    # I'll define the new HTML
    marquee_section = '''
    <div class="marquee-container">
        <div class="marquee-content">
            <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
            <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
            <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
            <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una" style="height: 80px;"></div>
            <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India"></div>
            <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
            
            <!-- Duplicate for loop -->
            <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
            <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
            <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
            <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una" style="height: 80px;"></div>
            <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India"></div>
            <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
        </div>
    </div>
    '''
    
    # I'll replace the existing container.
    # I'll search for the div that wraps `make_in_india`.
    # It probably starts with `<div` and ends with `</div>`.
    # I'll just use a fuzzy replace of the segment "from first image to last image".
    
    # Let's find the start of the first image tag and end of the last image tag in that group.
    # Images: make_in_india, digital_india, govt_of_india, iiit_una, swachh_bharat.
    
    # Finding start index of first image tag.
    # It might be `make_in_india` or another one first.
    # In step 2234 I added them.
    # In `index.html` (reverted state), they might be in a different order or just added.
    
    # I'll look for the substring `src="assets/make_in_india.svg"` to `src="assets/swachh_bharat.svg"` (or whatever is last).
    # Step 2661 output: `width-24-parent pr-60`.
    
    # I'll Try to replace the WHOLE Footer Grid if I can find it.
    # But since I can't guarantee the structure, I will replace the `div` containing `make_in_india`.
    
    # I'll write a script to identify the parent bounds and replace it.
    pass

footer_css = '''
<style>
/* MARQUEE STYLES */
.marquee-container {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    padding: 20px 0;
    background: transparent;
    position: relative;
    mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
    -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
}

.marquee-content {
    display: inline-flex;
    animation: marquee-scroll 20s linear infinite;
    align-items: center;
}

.marquee-item {
    margin: 0 40px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.marquee-item img {
    height: 60px;
    width: auto;
    object-fit: contain;
    filter: none;
    opacity: 0.9;
}

@keyframes marquee-scroll {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}
</style>
'''

with open('replace_footer_marquee.py', 'w', encoding='utf-8') as f:
    f.write(f'''
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert CSS
if "MARQUEE STYLES" not in html:
    html = html.replace('</head>', """{footer_css}""" + '</head>')

# Replace Content
# I'll find the div containing "assets/make_in_india.svg"
# And replace that whole DIV.
# regex: <div[^>]*>[^<]*<img[^>]*src="assets/make_in_india.svg".*?</div>
# This assumes they are all in ONE div.
# Based on screenshot, they are in a row.

# Logic: Find start of div wrapping make_in_india. Find matching closing div.
# This is hard with regex nesting.
# Instead, I will replace the CONTENT of the div.
# Searching for the sequence of images and replacing them with my Marquee Block.

# The sequence seems to be:
# img, img, img...
# Maybe in separate divs?
# "width-24-parent" suggests columns?

# I will replace the PARENT CONTAINER of "assets/make_in_india.svg".
# Look for `<div` before it.
# Look for `</div>` after the last image?

# Let's locate the range.
start_marker = 'assets/make_in_india.svg'
end_marker = 'assets/swachh_bharat.svg' # Based on screenshot order or likelihood

s_idx = html.find(start_marker)
e_idx = html.find(end_marker)

if s_idx != -1 and e_idx != -1:
    # Find the nearest opening div before s_idx
    # Find the closing div after e_idx
    
    # Just blanking out the whole region and inserting marquee.
    # Be careful not to delete too much.
    
    # Let's try to find the specific "container" class if possible.
    # If not, I'll replace the block covering these indices.
    
    # Actually, I'll replace from the `<div` preceding `make_in_india` to the `</div>` following `swachh_bharat`.
    
    # Approximate:
    pre_chunk = html[:s_idx]
    last_div_start = pre_chunk.rfind('<div')
    
    post_chunk = html[e_idx:]
    first_div_end = post_chunk.find('</div>') + 6 + e_idx
    
    # This might be just ONE element's div.
    # If they are siblings, I need the parent.
    
    # This is risky.
    # Safer plan:
    # Use the `dump_glitch_context.py` logic but for footer.
    # I'll extract it, verifying it locally, then replace.
    
    # But for now, I'll append the marquee AT THE END of the footer container?
    # No, user wants REPLACEMENT ("make it endless loop").
    
    # I'll blindly replace the text snippet matching the images I see in screenshot.
    # Pattern: <img.*?make_in_india.*?>.*<img.*?swachh_bharat.*?>
    # I'll try to construct a regex that captures all 4-5 images.
    
    # Regex: (<img[^>]*src="assets/(?:make_in_india|digital_india|govt_of_india|iiit_una_logo|swachh_bharat)[^"]*"[^>]*>\s*)+
    # I'll replace any occurrence of that sequence with my marquee.
    pass
''')
