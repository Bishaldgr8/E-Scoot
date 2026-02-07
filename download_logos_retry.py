
import requests
import os
import time

# URLs
logos = {
    # "iiit_una_logo.png": "http://iiitu.ac.in/assets/iiitu-logo-DvoK09sP.png", # Already have this
    "make_in_india.png": "https://upload.wikimedia.org/wikipedia/en/thumb/6/6a/Make_In_India.png/300px-Make_In_India.png",
    "govt_of_india.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Emblem_of_India.svg/200px-Emblem_of_India.svg.png",
    "swachh_bharat.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Swachh_Bharat_Abhiyan_logo.svg/300px-Swachh_Bharat_Abhiyan_logo.svg.png",
    "digital_india.png": "https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Digital_India_logo.svg/300px-Digital_India_logo.svg.png",
    "made_in_india_text.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Made_in_India_Logo.png/320px-Made_in_India_Logo.png"
}

output_dir = r"c:\Users\assdr\Desktop\New Project\assets"
os.makedirs(output_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for name, url in logos.items():
    if os.path.exists(os.path.join(output_dir, name)) and os.path.getsize(os.path.join(output_dir, name)) > 1000:
        print(f"Skipping {name}, already exists.")
        continue
        
    try:
        print(f"Downloading {name} from {url}...")
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            with open(os.path.join(output_dir, name), "wb") as f:
                f.write(response.content)
            print(f"Downloaded {name}")
        else:
            print(f"Failed to download {name} from {url}, status: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")
    time.sleep(2) # Delay to be nice
