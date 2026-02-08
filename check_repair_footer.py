
# The previous script detected duplicates and removed them? Wait, it just searched.
# The output said "Found 2 marquee blocks".
# And "Replacing range ... with Single Static + Marquee".
# But it didn't write the file. The script was set to write file at the end.
# Ah, the previous script `cleanup_footer_mess.py` actually ran `write` logic at the end.
# But it printed "Replacing range..."
# Let's verify if `index.html` was updated or if the script logic was just printing.

# The script body had `with open('index.html', 'w', encoding='utf-8') as f: f.write(html)` at the VERY end.
# So if it ran successfully, it improved.
# However, the output said "Remaining Make in India icons: 0".
# This means I deleted ALL icons.
# And then the script had logic "Assuming I need to add the Marquee BACK".
# Checks `matches`. If `matches` was truthy, it did replacement.

# Output: "Found 2 marquee blocks to remove." (Not 33?)
# Wait, `count_icons.py` said 33 containers.
# `cleanup_footer_mess.py` said 2 blocks.
# Maybe my regex for blocks failed to catch nested or broken ones?

# If `Remaining Make in India icons: 0`, then I wiped them out.
# So I need to ensure I put the `new_content` back.

# I will write `final_footer_restore.py` to Force Re-Insertion if missing.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check current state
count = html.count('assets/make_in_india.svg')
print(f"Current Count: {count}")

# HTML to Insert (Static + Marquee)
hybrid_footer = '''
<!-- Static Footer Row -->
<div class="footer-static-icons" style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 40px; padding: 40px 0;">
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

# Identify insertion point if count is 0.
# Look for `Made in India` text (not image)? Or `Copyright`? Or `Footer` class?
# I'll search for `class="footer"` or simply insert before `</body>`.

if count == 0:
    # Try to find a good place.
    # Previous place was likely inside a container.
    # I'll try to find `class="footer"` or `id="footer"`.
    # Or just `Script` tags at the end.
    
    # Let's search for "Swachh Bharat" text? No.
    # Search for "IIIT Una" text?
    
    # I'll just append it to the body for now, or trace where I deleted it.
    # The deletion was via regex `marquee-container`.
    # So the hole is where the marquee was.
    
    # If `cleanup_footer_mess.py` ran, it replaced correctly.
    # Why did it say "Found 2"?
    # Maybe because regex was `.*?` non-greedy but `re.DOTALL` matched across lines.
    # It might have collapsed them.
    
    # If `count` is now ~12 (6 static + 12 marquee = 18?), then we are good.
    # If count is 0, we need to insert.
    pass
elif count >= 18:
    print("Looks like we have content. Checking layout...")
    # Maybe Remove duplicates if still > 18.
    pass

# Force Animation CSS back (in case I stripped it in previous step).
css_check = 'animation: marquee-scroll'
if css_check not in html:
    # Add CSS
    # ...
    pass
