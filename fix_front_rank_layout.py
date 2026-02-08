
# The user sees a "Glitch" where "Front-rank" title and "We have front-rank facilities..." block overlap.
# This structure suggests they are stacking on top of each other.
# I will force them to stack VERTICALLY with spacing.

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_fix = '''
<style>
/* FIX FRONT RANK LAYOUT GLITCH */
.scroll-slide-section {
    position: relative !important;
    height: auto !important;
    display: block !important;
}

.intro-front-rank {
    position: relative !important;
    height: auto !important;
    margin-bottom: 50px !important;
    background-color: #2b2b2b !important; /* Ensure background hides anything behind */
    padding: 20px !important;
    z-index: 5 !important;
}

.slide-1, .slide-2 {
    position: relative !important;
    height: auto !important;
    margin-top: 20px !important;
    margin-bottom: 20px !important;
    opacity: 1 !important;
    transform: none !important;
    display: block !important;
    z-index: 4 !important;
}

.block-inner {
    opacity: 1 !important;
    position: relative !important;
}
</style>
'''

if "FIX FRONT RANK LAYOUT GLITCH" not in html:
    html = html.replace('</head>', css_fix + '</head>')
    print("Injected Front-Rank layout fix.")
else:
    print("Front-Rank layout fix already exists.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
