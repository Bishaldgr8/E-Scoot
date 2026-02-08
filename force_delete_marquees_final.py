
# Validating regex failure: 2 occurrences found.
# I will use a custom parser to remove them to be safe.
# Find start index, find end index (matching div depth or just known structure).
# Since I inserted them, I know the structure:
# <div class="marquee-container">
# ..
# </div> (end of container)

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove loop until no marquee-container is found.
while True:
    start = html.find('<div class="marquee-container">')
    if start == -1:
        break
    
    # Find the end.
    # It should be `</div>` followed by `</div>`?
    # Or just `</div>` of the container.
    # The structure: <div class="marquee-container"> <div class="marquee-content"> ... </div> </div>
    # So 2 closing divs.
    
    # Let's simple find the next `</div></div>` sequence?
    # Or count open/close divs?
    
    current = start + len('<div class="marquee-container">')
    depth = 1
    end = -1
    
    # Simple parser to find matching </div>
    while current < len(html):
        next_open = html.find('<div', current)
        next_close = html.find('</div>', current)
        
        if next_close == -1:
            print("Error: Could not find closing div")
            break
            
        if next_open != -1 and next_open < next_close:
            depth += 1
            current = next_open + 4
        else:
            depth -= 1
            current = next_close + 6
            if depth == 0:
                end = current
                break
    
    if end != -1:
        print(f"Removing block from {start} to {end}")
        html = html[:start] + html[end:]
    else:
        print("Could not parse block end. Aborting safety removal.")
        break

# Now insert ONE clean marquee.
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

html = html.replace('</body>', marquee_html + '\n</body>')
print("Inserted one clean marquee.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
