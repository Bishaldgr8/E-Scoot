
# Validating context:
# --- Context for Arnpre ---
# ... iv><h4 style="op
# (base)iv><h4 style="op... Arnpreet Y

# It seems the name is in an `<h4>` tag.
# `<h4 style="...">Arnpreet Y</h4>`
# And there is a `div` wrapper around it?
# `...iv><h4 ...`

# I will use a robust replacement:
# Find `Arnpreet Y` etc.
# Find the opening `<` of the tag containing it.
# Insert Quote before that tag.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

quotes = {
    "Arnpreet Y": "Hard work are the FEET of success",
    "Bishal B": "Doesn't matter yaar",
    "Ambatokandh Singh": "AMBTK!",
    "Rapunzal S": "You only see what we show"
}

# CSS:
quote_css = '''
<style>
    .team-quote {
        position: absolute;
        top: 40%; /* Slightly above center */
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90%;
        text-align: center;
        color: #fff;
        font-size: 1.4rem;
        font-weight: bold;
        background: rgba(0, 0, 0, 0.8); /* Darker for readability */
        padding: 20px;
        border-radius: 10px;
        opacity: 0;
        transition: opacity 0.4s ease, transform 0.4s ease;
        pointer-events: none;
        z-index: 20;
        font-family: inherit;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    .team-quote::after {
        content: '"';
        display: block;
        font-size: 2rem;
        line-height: 1;
        margin-top: 10px;
        opacity: 0.5;
    }
    
    .team-quote::before {
        content: '"';
        display: block;
        font-size: 2rem;
        line-height: 1;
        margin-bottom: 5px;
        opacity: 0.5;
    }

    .swiper-slide:hover .team-quote {
        opacity: 1;
        transform: translate(-50%, -60%); /* Slight movement up */
    }
    
    /* Ensure parent has relative positioning */
    .swiper-slide {
        position: relative;
    }
</style>
'''

if '.team-quote' not in html:
    html = html.replace('</head>', quote_css + '\n</head>')
    print("Injected CSS.")

# Replacement Logic
for name, quote in quotes.items():
    # Find the Name string.
    # Regex to find the tag surrounding it.
    # <tag ... > Name </tag>
    # or just text node.
    
    # I'll use `re.sub` with a pattern matching the name and capturing the tag start.
    # Pattern: `(<[^>]*>\s*Arnpreet Y\s*</[^>]*>)` matches the whole element.
    # E.g. `<h4>Arnpreet Y</h4>`.
    
    pattern = re.compile(r'(<[^>]*>\s*' + re.escape(name) + r'\s*</[^>]*>)', re.IGNORECASE)
    
    if pattern.search(html):
        q_html = f'<div class="team-quote">{quote}</div>'
        # Insert BEFORE the name element.
        # So it sits in the slide, above the text (DOM-wise, but absolute positioned).
        # Actually, `top: 40%` aligns it relative to slide.
        
        html = pattern.sub(f'{q_html}\n\\1', html)
        print(f"Added quote for {name}.")
    else:
        print(f"Regex failed for {name}. Usage simple replace?")
        # Fallback: Just replace the name text with `</div>quote<div>name`?
        # No, that breaks tags.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
