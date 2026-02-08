
# Suspicion: User is viewing `team.html`, not `index.html`.
# I will check if `team.html` exists and has the slider code.

import os

if os.path.exists('team.html'):
    print("Found team.html. Reading content...")
    with open('team.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'swiper-container' in html:
        print("team.html contains Swiper code.")
        # check if it has the old width
        if 'width: 279px' in html:
            print("team.html HAS the old 279px width restriction!")
        else:
            print("team.html does not have 279px width (maybe clean?).")
            
        # Check if it has my new quote injection?
        if 'team-quote' in html:
            print("team.html HAS quotes code.")
        else:
            print("team.html MISSING quotes code (So my previous scripts didn't touch it!)")
            
    else:
        print("team.html does NOT contain Swiper code.")

else:
    print("team.html does not exist.")
