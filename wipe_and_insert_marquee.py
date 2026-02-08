
# Count of Marquee Containers: 2.
# This confirms DUPLICATION.
# I likely appended a marquee in `reinsert_footer.py` while one was already there (from `cleanup_footer_mess.py` logic which might have failed to wipe everything?).
# Or `cleanup` wiped "duplicate marquees" but kept ONE, and then `reinsert` ADDED ANOTHER?

# Solution:
# Delete ALL `marquee-container` blocks.
# Insert ONE fresh one.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove ALL marquee containers.
pattern = re.compile(r'<div class="marquee-container">.*?</div>\s*</div>', re.DOTALL)
html = pattern.sub('', html)
print("Wiped all marquee containers.")

# Insert ONE fresh marquee.
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

# Insert before `</body>` or `last </div>`?
# I'll just replace `</body>` with `marquee + </body>`.
html = html.replace('</body>', marquee_html + '\n</body>')
print("Inserted clean marquee.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
