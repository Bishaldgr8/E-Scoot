
# User wants quotes on hover for Team Members.
# Quotes:
# Arnpreet Y -> "Hard work are the FEET of success"
# Bishal B -> "Doesn't matter yaar"
# Ambatokandh Singh -> "AMBTK!"
# Rapunzal S -> "You only see what we show"

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the members and their quotes.
# I need to find the specific slide for each.
# I'll look for the Name and insert the Quote HTML nearby.
# The structure usually is:
# <div class="swiper-slide">
#   ...
#   <div class="name">Arnpreet Y</div>
#   ...
# </div>

quotes = {
    "Arnpreet Y": "Hard work are the FEET of success",
    "Bishal B": "Doesn't matter yaar",
    "Ambatokandh Singh": "AMBTK!",
    "Rapunzal S": "You only see what we show"
}

# CSS to inject for the quotes.
# Position absolute, center or bottom?
# "moved towards the member" -> Hover.
quote_css = '''
<style>
    .team-quote {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 80%;
        text-align: center;
        color: #fff;
        font-size: 1.2rem;
        font-weight: bold;
        background: rgba(0, 0, 0, 0.7);
        padding: 15px;
        border-radius: 8px;
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none; /* Let clicks pass through */
        z-index: 10;
        font-family: 'Outfit', sans-serif; /* Matching theme if possible */
    }

    .swiper-slide:hover .team-quote {
        opacity: 1;
    }
</style>
'''

# Inject CSS if not present.
if '.team-quote' not in html:
    html = html.replace('</head>', quote_css + '\n</head>')
    print("Injected Quote CSS.")

# Inject Quotes into HTML.
for name, quote in quotes.items():
    # Find the Name div.
    # Pattern: `>Name</div>` or `>Name <` 
    # The name might be split across lines or tags?
    # Based on previous edits, text is likely clean: `>Arnpreet Y</div>`
    
    # I want to insert the quote DIV inside the same `swiper-slide`.
    # I can insert it right before the `.name` div? Or after?
    # If I insert it inside the slide container, absolute text works.
    
    # Search for the name.
    # Use simple string search first.
    name_idx = html.find(name)
    if name_idx == -1:
        # Try partial?
        print(f"Warning: Could not find exact name '{name}'. Skipping.")
        continue
    
    # Trace back to find parent `swiper-slide`?
    # Or just insert before the name tag.
    # If the setup is `<div class="name">Name</div>`, inserting before is safe for absolute positioning (relative to slide).
    
    # Construct Quote HTML
    q_html = f'<div class="team-quote">"{quote}"</div>'
    
    # Insert before the name.
    # Look for the tag opening before the name. `<div class="name">` or similar.
    # I'll search backwards from `name_idx` for `<div`.
    
    # Better: regex replace to target the block.
    # Pattern: (<div[^>]*class="[^"]*name"[^>]*>\s*Arnpreet Y\s*</div>)
    # Replace with: Quote + \1
    
    pattern = re.compile(r'(<div[^>]*class="[^"]*name"[^>]*>\s*' + re.escape(name) + r'\s*</div>)', re.IGNORECASE)
    
    if pattern.search(html):
        # Check if quote already exists? (To avoid duplicate if script runs twice)
        # If I see `team-quote` nearby, skip?
        # But for now, simple replace.
        html = pattern.sub(f'{q_html}\n\\1', html)
        print(f"Added quote for {name}.")
    else:
        print(f"Regex failed for {name}. Checking manually.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
