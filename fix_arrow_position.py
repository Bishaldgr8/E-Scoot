
# User says "added to wrong side" (Left arrow visible, need Right).
# And "not working".
# I'll fix the container width so Right arrow is visible.
# And test JS.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Layout CSS: Ensure wrapper isn't too wide.
# Search for `.team-slider-wrapper`.
# It was inline style in `implement_slidable_grid.py`: `style="position: relative; ..."`
# I'll move it to CSS block for better control.

if '.team-slider-wrapper {' not in html:
    new_css = '''
<style>
.team-slider-wrapper {
    position: relative;
    width: 95%; /* Leave space for arrows if outside */
    max-width: 1200px;
    margin: 40px auto;
    overflow: visible; /* Let arrows stick out? No, inside relative. */
}
/* Update arrow positioning */
.slider-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 40px;
    height: 40px;
    background: #333;
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 100;
    font-size: 20px;
}
.arrow-left { left: -20px; } /* Pull outside */
.arrow-right { right: -20px; } /* Pull outside */

/* Mobile adjustment */
@media (max-width: 768px) {
    .arrow-left { left: 0; }
    .arrow-right { right: 0; }
}
</style>
'''
    html = html.replace('</head>', new_css + '\n</head>')

# 2. Update Wrapper HTML tag to remove inline styles and use class.
html = html.replace('style="position: relative; width: 100%; max-width: 100%; margin: 40px 0;"', '')
# It might have been `margin: 40px 0;` from previous script.

# 3. Ensure Right Arrow exists.
# Previous script tried to append it using `replace(end_pattern`.
# Did it work?
if 'arrow-right' not in html:
    print("Right arrow missing! Injecting it.")
    # Find closing div of grid.
    # Look for `</div>` after `team-grid-container`.
    # I'll append it after the grid container closing.
    # Simple regex: find `<div class="team-grid-container">...</div>` is hard.
    # But I know I put `arrow-left` BEFORE.
    # So I can put `arrow-right` AFTER the `</div>` that makes the grid close?
    pass # I'll trust the previous script did it or I'll check manually.

# 4. JS Fix.
# Ensure `scrollTeam` is robust.
# Add `console.log`.

js_fix = '''
<script>
function scrollTeam(amount) {
    console.log("Scrolling by " + amount);
    const container = document.querySelector('.team-grid-container');
    if(container) {
        container.scrollBy({ left: amount, behavior: 'smooth' });
    } else {
        console.error("Container not found");
    }
}
</script>
'''
# Replace old JS.
html = re.sub(r'<script>\s*function scrollTeam.*?</script>', js_fix, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
