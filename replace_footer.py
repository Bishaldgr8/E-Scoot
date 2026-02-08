
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for Marquee
marquee_css = '''
<style>
/* MARQUEE STYLES */
.marquee-container {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    padding: 30px 0;
    margin-top: 20px;
    background: transparent;
    position: relative;
    /* Fade edges */
    mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
    -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
}

.marquee-content {
    display: inline-flex;
    animation: marquee-scroll 25s linear infinite;
    align-items: center;
}

/* Pause on hover for accessibility */
.marquee-content:hover {
    animation-play-state: paused;
}

.marquee-item {
    margin: 0 40px; /* Gap between icons */
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.marquee-item img {
    height: 70px; /* Consistent height */
    width: auto;
    max-width: 180px;
    object-fit: contain;
    filter: none; /* Keep original colors as requested (or implied by 'icons') */
    opacity: 1;
    transition: transform 0.3s;
}

.marquee-item img:hover {
    transform: scale(1.1);
}

@keyframes marquee-scroll {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); } 
}
</style>
'''

# HTML for Marquee (Set 1 + Set 2)
# I will use distinct classes for items to allow potential future styling.
marquee_html = '''
<div class="marquee-container">
    <div class="marquee-content">
        <!-- Set 1 -->
        <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India" style="height: 90px;"></div>
        <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
        
        <!-- Set 2 (Duplicate) -->
        <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India" style="height: 90px;"></div>
        <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
    </div>
</div>
'''

# Insert CSS
if "MARQUEE STYLES" not in html:
    html = html.replace('</head>', marquee_css + '</head>')
    print("Injected Marquee CSS.")

# Replace Footer Icons
# I will aggressively find the block containing `assets/make_in_india.svg` and siblings.
# Since I couldn't get the exact parent div easily, I will replace a matched chunk of lines.

# Search for the block starting near Make in India
start_idx = html.find('assets/make_in_india.svg')
if start_idx != -1:
    # Find the START of the div container.
    # Look backwards for `<div`
    # I'll search backwards 500 chars and look for `<div class="...` 
    # Or just the nearest `<div`.
    
    # Actually, simpler: finding the `wrapper` div by class is hard if I don't know it.
    # Step 2661 showed: `width-24-parent pr-60`.
    # Let's search for THAT class string.
    
    parent_search = html.rfind('<div', 0, start_idx)
    # This gives me the immediate parent (likely text-center or similar).
    
    # I'll assume the image is inside a `.marquee-item` or similar structure from previous steps? 
    # No, previous step was revert.
    
    # I will replace the containing DIV of `make_in_india`.
    # I'll grab 500 chars before and after.
    # And replace from the Start of the Div to the End of the Div.
    
    # Find opening div
    # <div ...> ... <img src="assets/make_in_india.svg" ... </div>
    
    # This is tricky without a DOM parser.
    # I'll try to find the `width-24-parent` class if it exists.
    # If not, I'll replace the Text segment roughly.
    
    # Let's try to match the sequence of images with regex.
    # Matches: <img ... make_in_india ...> (anything in between) <img ... swachh_bharat ...>
    # And replace that WHOLE sequence with my MARQUEE HTML.
    
    # This keeps the container but replaces content.
    regex_pattern = r'(<img[^>]*src="assets/make_in_india\.svg"[^>]*>).*?(<img[^>]*src="assets/swachh_bharat\.svg"[^>]*>)'
    
    match = re.search(regex_pattern, html, re.DOTALL)
    if match:
        # We found the block of images.
        # Check if there are other images in between.
        # replace the match with marquee_html
        
        # BUT waait, I should replace the PARENT DIV if possible to remove existing styling (grid columns etc).
        # Use the match start to find parent div.
        
        s = match.start()
        e = match.end()
        
        # Look backwards for <div
        div_start = html.rfind('<div', 0, s)
        # Look forwards for </div>
        div_end = html.find('</div>', e) + 6
        
        # Verify this is the right div. 
        # If the segment is small (< 1000 chars), it's likely the specific container.
        if (div_end - div_start) < 2000:
            # Replace the whole div
            repl_target = html[div_start:div_end]
            html = html.replace(repl_target, marquee_html)
            print("Replaced footer icon container with Marquee.")
        else:
            # Container too big (might be entire footer), just replace images.
            html = html[:s] + marquee_html + html[e:]
            print("Replaced image sequence with Marquee (Container kept).")

    else:
        # Try finding simpler sequence
        print("Complex regex failed. Trying simple replace.")
        # Just replace the first occurrence of the image tag with the whole marquee, and delete others?
        # Risky.
        
        # Let's just find `assets/make_in_india.svg` tag and replace ITS PARENT.
        
        pass

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
