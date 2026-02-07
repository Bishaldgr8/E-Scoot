import os
import re
import urllib.request
from urllib.parse import urljoin, urlparse
import shutil

# Configuration
SOURCE_FILE = 'source.html'
OUTPUT_FILE = 'index.html'
ASSETS_DIR = 'assets'
BASE_URL = 'https://ujet-wip-2020.webflow.io/'

# Ensure assets directory exists
if not os.path.exists(ASSETS_DIR):
    os.makedirs(ASSETS_DIR)

def download_file(url, folder):
    try:
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            return None
        # Handle query parameters or duplicate names if necessary
        filepath = os.path.join(folder, filename)
        
        # Don't re-download if exists
        if os.path.exists(filepath):
            return filepath
            
        print(f"Downloading {url}...")
        
        # Add headers to mimic browser
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        )
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        return filepath
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def process_html():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex patterns to find URLs
    # 1. src="..." in img, script, source
    # 2. href="..." in link (css, favicon)
    # 3. data-bg="..." (custom attribute)
    # 4. data-src="..." (lottie or lazy load)
    
    # We will replace matched URLs with local paths
    
    # CSS Files
    # Note: We already downloaded webflow.css manually, so we just map it.
    # main.css was broken (403), so we will comment it out or point to a valid one if we had it.
    content = content.replace('https://assets.website-files.com/5f3f94975bc16014c13c0c36/css/ujet-wip-2020.9731f93be.css', 'webflow.css')
    content = content.replace('https://dl.dropbox.com/s/fqwjz1zmtli5so1/main.css', '/* main.css broken */')
    
    # JS Files
    content = content.replace('https://assets.website-files.com/5f3f94975bc16014c13c0c36/js/ujet-wip-2020.cd7b66d90.js', 'webflow.js')
    content = content.replace('https://dl.dropbox.com/s/29c9e7d610g08qo/main.js', '/* main.js broken */')

    # Images and Assets
    # Find all http/https URLs that look like assets
    url_pattern = re.compile(r'(https?://[^"\')\s>]+(?:\.png|\.jpg|\.jpeg|\.svg|\.gif|\.json|\.ico))', re.IGNORECASE)
    
    urls = set(url_pattern.findall(content))
    
    for url in urls:
        # Skip if it's already processed or is a css/js we handled manually
        if 'css' in url or 'js' in url:
            continue
            
        print(f"Processing asset: {url}")
        local_path = download_file(url, ASSETS_DIR)
        
        if local_path:
            # Replace in content - using relative path for browser
            # Escape the URL for regex replacement
            relative_path = f"assets/{os.path.basename(local_path)}"
            content = content.replace(url, relative_path)

    # Save output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Done. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    process_html()
