
import re

file_path = r"c:\Users\assdr\Desktop\New Project\index.html"

new_html = """
<div class="logo-marquee">
    <div class="logo-track">
        <!-- Set 1 -->
        <div class="logo-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="logo-item"><img src="assets/govt_of_india.png" alt="Government of India"></div>
        <div class="logo-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="logo-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="logo-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="logo-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
        
        <!-- Set 2 -->
        <div class="logo-item"><img src="assets/iiit_una_logo.png" alt="IIIT Una"></div>
        <div class="logo-item"><img src="assets/govt_of_india.png" alt="Government of India"></div>
        <div class="logo-item"><img src="assets/make_in_india.svg" alt="Make in India"></div>
        <div class="logo-item"><img src="assets/swachh_bharat.svg" alt="Swachh Bharat"></div>
        <div class="logo-item"><img src="assets/digital_india.svg" alt="Digital India"></div>
        <div class="logo-item"><img src="assets/made_in_india.svg" alt="Made in India"></div>
    </div>
</div>
"""

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find start
start_marker = '<div class="logo-parent-w">'
end_marker = '<div class="footer-parent">'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    print(f"Replacing content from {start_idx} to {end_idx}")
    # We replace everything from start_marker up to end_marker
    # We need to check if there are closing divs before "footer-parent" that we should remove or keep.
    # The structure was `...</div></div><div class="footer-parent">`
    # The `</div></div>` likely closed `logo-parent-w` and maybe a container above it? or just `logo-parent-w`?
    # `logo-parent-w` starts with 1 div.
    # If `content[end_idx-12:end_idx]` is `</div></div>`, then we are likely removing `logo-parent-w` and its parent?
    # Actually, let's look at what `inspect_logo_block.py` showed.
    # It showed `<div class="logo-parent-w">`
    
    # I will assume that I should replace from `start_marker` up to `end_marker`. 
    # But I should verify what I am removing.
    
    # Let's try to identify the exact block to remove.
    # If I just replace `start_marker`... `end_marker`, I might be removing closing divs that belong to `logo-parent-w` (good) or parents (bad).
    
    # Let's assume `logo-parent-w` is a self-contained block followed by `footer-parent`.
    # I will replace `content[start_idx:end_idx]` with `new_html`.
    # But `new_html` does not have standard closing divs if `logo-parent-w` required them.
    # `logo-parent-w` is a div.
    # If the original HTML had `</div></div>` before `footer-parent`, one `</div>` is for `logo-parent-w`.
    # What is the other for?
    
    # Let's peek at the content before `footer-parent`
    print("Content before footer-parent:", content[end_idx-20:end_idx])
    
    # If it is `</div></div>`, and I replace from `start_marker` (which is `<div class="logo-parent-w">`),
    # I am removing the OPENING of `logo-parent-w` and everything inside.
    # I need to know where `logo-parent-w` ends.
    # If I replace until `footer-parent`, I am removing everything between them.
    
    # Safe bet: The new marquee is a block element.
    # I will replace `content[start_idx:end_idx]` with `new_html + "</div>" * N`? No.
    
    # Let's use the `find_div_end` logic to find where `logo-parent-w` ends, and replace THAT.
    
    def find_div_end_func(s, start_idx):
        count = 1
        i = start_idx + 1
        while count > 0 and i < len(s):
            if s[i:i+4] == '<div':
                count += 1
                i += 4
            elif s[i:i+6] == '</div>':
                count -= 1
                i += 6
            else:
                i += 1
        return i

    block_end = find_div_end_func(content, start_idx + 4) # +4 to skip `<div`
    print(f"Calculated block end at {block_end}")
    
    # Check if there are other things between block_end and footer-parent.
    # If block_end < end_idx, there is stuff in between.
    
    if block_end <= end_idx:
        print("Replacing calculated block.")
        new_content = content[:start_idx] + new_html + content[block_end:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Replacement successful.")
    else:
        print("Block end is AFTER footer starts? Something is wrong.")
        
else:
    print("Markers not found.")
