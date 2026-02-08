
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert CSS
if "MARQUEE STYLES" not in html:
    html = html.replace('</head>', """
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
""" + '</head>')

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
