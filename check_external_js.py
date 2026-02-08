
# Validating if Swiper is initialized in external JS.
# Also checking server.py.

import os
import re

files_to_check = ['animations.js', 'script.js', 'main.js', 'app.js', 'server.py']

for fname in files_to_check:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"--- {fname} found ---")
        
        # Check for Swiper
        if 'new Swiper' in content:
            print(f"!!! Swiper init found in {fname} !!!")
            # Print context
            matches = re.findall(r'new Swiper\([^)]*\)', content)
            for m in matches:
                print(m)
                
        # Check for server logic
        if fname == 'server.py':
            print("Server content snippet:")
            print(content[:500]) # First 500 chars

    else:
        # print(f"{fname} not found.")
        pass
