
# Replace the Swiper Section with a Static Grid.
# Robust strategy: Find start of swiper-container, count divs to find end.

import re

team_data = [
    {"name": "Arnpreet Y", "role": "Chief Executive Officer", "quote": "Hard work are the FEET of success", "img": "assets/team_arnpreet.jpg"},
    {"name": "Bishal B", "role": "Co-Founder", "quote": "Doesn't matter yaar", "img": "assets/team_bishal.jpg"},
    {"name": "Ambatokandh Singh", "role": "Chief Technology Officer", "quote": "AMBATKAM!", "img": "assets/team_ambatokandh.jpg"},
    {"name": "Rapunzal S", "role": "Chief Marketing Officer", "quote": "You only see what we show", "img": "assets/team_rapunzal.jpg"}
]

# New HTML
new_html_block = '''
<div class="team-grid-container">
'''

for member in team_data:
    new_html_block += f'''
    <div class="team-card">
        <div class="image-wrapper">
            <img src="{member['img']}" alt="{member['name']}">
            <div class="team-quote">"{member['quote']}"</div>
        </div>
        <div class="team-info">
            <h4>{member['name']}</h4>
            <div class="role">{member['role']}</div>
        </div>
    </div>
'''

new_html_block += '</div>'

# New CSS
new_css = '''
<style>
/* Team Grid Styles */
.team-grid-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 20px;
    width: 100%;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
    flex-wrap: wrap; /* Responsive wrap */
}

.team-card {
    width: 23%; /* 4 items fit */
    min-width: 250px; /* Stack on mobile */
    position: relative;
    box-sizing: border-box;
    margin-bottom: 30px;
}

.image-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 3/4;
    overflow: hidden;
    border-radius: 8px; /* Optional aesthetics */
}

.image-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
}

/* Quote Overlay */
.team-quote {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90%;
    text-align: center;
    color: #fff;
    font-size: 1.2rem;
    font-family: serif;
    font-style: italic;
    opacity: 0;
    transition: opacity 0.3s ease;
    pointer-events: none;
    z-index: 10;
    text-shadow: 0 2px 4px rgba(0,0,0,0.8);
}

.team-card:hover .team-quote {
    opacity: 1;
}

.team-card:hover img {
    transform: scale(1.05);
    filter: brightness(0.4); /* Darken image to read quote */
}

/* Info Logic */
.team-info {
    margin-top: 15px;
    text-align: left;
    transition: opacity 0.3s;
}

.team-card:hover .team-info {
    opacity: 0.3; /* Fade out slightly? Or hide completely as requested? User: "older text... to DISAPPEAR" */
    opacity: 0 !important; 
}

h4 { margin: 0; font-size: 1.2rem; color: #fff; }
.role { font-size: 0.9rem; color: #ccc; margin-top: 5px; }

/* Mobile Responsiveness */
@media (max-width: 768px) {
    .team-card { width: 48%; }
}
@media (max-width: 480px) {
    .team-card { width: 100%; }
}
</style>
'''

# Replacement Logic
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find start of swiper-container.
# Look for `<div` followed by `class="...swiper-container..."`
start_marker = 'class="swiper-container"'
start_idx = html.find(start_marker)

if start_idx == -1:
    print("Error: Could not find swiper-container.")
else:
    # Find the opening `<div` before `start_idx`.
    # Scan backwards.
    open_tag_idx = html.rfind('<div' , 0, start_idx)
    
    if open_tag_idx == -1:
        print("Error: Could not find opening div tag.")
    else:
        # Now count divs from open_tag_idx + 4.
        # depth = 1.
        current_pos = open_tag_idx + 4
        depth = 1
        
        while depth > 0 and current_pos < len(html):
            next_open = html.find('<div', current_pos)
            next_close = html.find('</div>', current_pos)
            
            if next_close == -1:
                print("Error: Unclosed divs.")
                break
                
            if next_open != -1 and next_open < next_close:
                depth += 1
                current_pos = next_open + 4
            else:
                depth -= 1
                current_pos = next_close + 6 # len('</div>')
        
        if depth == 0:
            end_idx = current_pos
            print(f"Replacing content from {open_tag_idx} to {end_idx} (Length: {end_idx - open_tag_idx})")
            
            # Replace!
            new_full_html = html[:open_tag_idx] + new_html_block + html[end_idx:]
            
            # Inject CSS
            new_full_html = new_full_html.replace('</head>', new_css + '\n</head>')
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(new_full_html)
            print("Successfully replaced team section.")
        else:
            print("Error: Parsing HTML depth failed.")
