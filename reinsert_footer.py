
# Count is 0. I need to Insert the Footer Content back.
# I will append it before `</body>` or inside `<footer>` if I can find it.
# I'll search for `class="footer"` or simply insert before `</body>`.

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
    mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
    -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
}

.marquee-content {
    display: inline-flex;
    animation: marquee-scroll 25s linear infinite;
    align-items: center;
}

.marquee-content:hover {
    animation-play-state: paused;
}

.marquee-item {
    margin: 0 40px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.marquee-item img {
    height: 70px;
    width: auto;
    max-width: 180px;
    object-fit: contain;
    filter: none;
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

# HTML Content (Static + Marquee)
hybrid_footer = '''
<!-- Static Footer Row -->
<div class="footer-static-icons" style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 40px; padding: 40px 0; background-color: #fff;">
    <img src="assets/make_in_india.svg" alt="Make in India" style="height: 60px;">
    <img src="assets/iiit_una_logo.png" alt="IIIT Una" style="height: 60px;">
    <img src="assets/govt_of_india.png" alt="Govt of India" style="height: 80px;">
    <img src="assets/digital_india.svg" alt="Digital India" style="height: 60px;">
    <img src="assets/swachh_bharat.svg" alt="Swachh Bharat" style="height: 60px;">
    <img src="assets/made_in_india.svg" alt="Made in India" style="height: 60px;">
</div>

<!-- Endless Marquee Animation -->
<div class="marquee-container">
    <div class="marquee-content">
        <!-- Set 1 -->
        <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India" style="height: 90px;"></div>
        <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
        
        <!-- Set 2 -->
        <div class="marquee-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="marquee-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="marquee-item"><img src="assets/govt_of_india.png" alt="Govt of India" style="height: 90px;"></div>
        <div class="marquee-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="marquee-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="marquee-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
    </div>
</div>
'''

# 1. Ensure CSS is present
if "MARQUEE STYLES" not in html:
    html = html.replace('</head>', marquee_css + '</head>')
    print("Injected CSS.")

# 2. Insert Content
# I'll try to find the `intro-front-rank` closing div? No bad idea.
# I'll look for `class="footer"`?
idx = html.rfind('footer')
# If found, try to put inside?

# Simpler: Look for `<script src="js/jquery...` or similar scripts at bottom.
# Insert BEFORE scripts but AFTER main content.
# Typically before `<script`.

script_idx = html.find('<script src')
if script_idx != -1:
    # Insert before first script tag?
    # Make sure it's not in head.
    # Find last occurrence of `</div>`.
    
    # Just insert it before `</body>`.
    # Layout might be weird if outside wrapper, but it works for now.
    
    html = html.replace('</body>', hybrid_footer + '\n</body>')
    print("Appended Footer Content before body end.")
else:
    # Fallback
    html = html.replace('</html>', hybrid_footer + '</html>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
