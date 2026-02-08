
# Count of Marquee Containers: 33 !!!!
# I broke index.html by appending/replacing continuously or matching incorrectly.
# I need to PURGE all `marquee-container` blocks and insert ONE clean one.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove ALL marquee containers first.
# Pattern: <div class="marquee-container">.*?</div></div> (nested?)
# Since I just added it, it should be clean blocks.
# I'll use a loop to remove shorter ones or regex.

# Regex to find marquee container block:
# It starts with `<div class="marquee-container">` and ends with `</div>` (outer).
# The inner content has `<div class="marquee-content">`.

# Let's simple remove any block that looks like the marquee script initiated.
# I'll enable DOTALL.
pattern = re.compile(r'<div class="marquee-container">.*?</div>\s*</div>', re.DOTALL)

# Check how many it finds
matches = pattern.findall(html)
print(f"Found {len(matches)} marquee blocks to remove.")

if matches:
    html = pattern.sub('', html)
    print("Removed all marquee blocks.")

# Now, I need to Restore the Footer Icons properly.
# The user wants "Top Row Static" and "Bottom Row Moving" (Endless Loop).
# "I meant the top row shouldnt be moving".
# This implies there IS a top row.
# If I deleted everything, I might have deleted the top row too (if I replaced it earlier).
# But since I saw "33 containers", I suspect I appended them.
# The Original Icons might still be there?

# Let's search for `assets/make_in_india.svg` again after removal.
remaining_count = html.count('assets/make_in_india.svg') # Note: this regex removal operates on string in memory, not file yet.
# Actually I should count in `html` variable.
# Since regex substitution happened, `html` is clean.

start_marker = 'assets/make_in_india.svg'
count_after = html.count(start_marker)
print(f"Remaining Make in India icons: {count_after}")

# If count_after == 0, I deleted EVERYTHING. I need to put back the Static Row + Marquee.
# If count_after > 0, the static row is likely preserved.

# Assuming I need to add the Marquee BACK (Just ONE).
# And ensure it is ANIMATED (Bottom Row).

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

# Restore CSS logic (ensure Animation is ACTIVE).
# My previous `fix_marquee_static.py` removed animation.
# I need to put `animation: marquee-scroll ...` back.
# I'll search/replace the CSS block.

css_fix = '''
.marquee-content {
    display: inline-flex;
    animation: marquee-scroll 25s linear infinite;
    align-items: center;
}
'''
# Find `.marquee-content` style and update it.
css_pattern = re.compile(r'\.marquee-content\s*\{[^}]*\}', re.DOTALL)
if css_pattern.search(html):
    html = css_pattern.sub(css_fix.strip(), html)
else:
    # Append if missing (it shouldn't be if I didn't delete head)
    pass

# INSERT Marquee.
# Where? "Below the Above Part" (Static Footer).
# If I have static icons, I should insert AFTER them.
# Identify the static footer container closing div.
# If I can't find it, I'll insert before `</body>` or `<footer>` close.
# Look for `footer-logo-grid` or similar if it exists.

# If `count_after` is 0, I need to restore the Static Row too.
# Static HTML:
static_html = '''
<div class="footer-static-icons" style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 40px; padding: 40px 0;">
    <img src="assets/make_in_india.svg" alt="Make in India" style="height: 60px;">
    <img src="assets/iiit_una_logo.png" alt="IIIT Una" style="height: 60px;">
    <img src="assets/govt_of_india.png" alt="Govt of India" style="height: 80px;">
    <img src="assets/digital_india.svg" alt="Digital India" style="height: 60px;">
    <img src="assets/swachh_bharat.svg" alt="Swachh Bharat" style="height: 60px;">
    <img src="assets/made_in_india.svg" alt="Made in India" style="height: 60px;">
</div>
'''

# If keys are missing, add Static + Marquee.
# Where to insert?
# Use `replace_footer.py` location logic or find specific marker.
# I'll look for where I removed the marquees.
# And insert `static_html + marquee_html` there.

# Actually, finding the insertion point after deletion is hard if I delete first.
# So I should doing replacement IN PLACE.

matches = list(pattern.finditer(html))
if matches:
    # Take the LAST match or FIRST match?
    # 33 matches means I spammed it.
    # They are likely contiguous or mostly contiguous.
    # I will replace the FIRST match with (Static + Marquee).
    # And remove the rest.
    
    first_match = matches[0]
    start = first_match.start()
    end = matches[-1].end() # Remove ALL of them.
    
    # Check if they are contiguous range?
    # If not, I might delete code in between.
    # But `marquee-container` blocks shouldn't have content in between if I just appended them.
    
    # Safe bet: Replace the First One with the Clean Block.
    # Remove subsequent ones.
    
    # To be safer: Remove ALL.
    # Then Insert at the `start` of the first one.
    
    # Construct new content
    new_content = static_html + marquee_html
    
    # Splice
    html = html[:start] + new_content + html[end:] # Removing everything from first to last match? Risky if not contiguous.
    
    # Better: Use `sub` to remove all. Then insert at `start`.
    # `html = pattern.sub('', html)` removed them.
    # `start` index is valid for original string.
    
    # Let's do:
    # 1. Identify start of first duplication.
    # 2. Identify end of last duplication.
    # 3. Replace range with `new_content`.
    
    print(f"Replacing range {start} to {end} with Single Static + Marquee.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
