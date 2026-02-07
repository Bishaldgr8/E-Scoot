
import os

assets_dir = r"c:\Users\assdr\Desktop\New Project\assets"

# Make in India SVG
make_in_india_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
  <rect width="100%" height="100%" fill="none"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="24" fill="#333">MAKE IN INDIA</text>
  <path d="M40,50 L160,50" stroke="#FF9933" stroke-width="2" transform="translate(0, 15)"/>
</svg>"""

# Swachh Bharat SVG (Glasses)
swachh_bharat_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
  <circle cx="70" cy="50" r="15" stroke="#333" stroke-width="3" fill="none"/>
  <circle cx="130" cy="50" r="15" stroke="#333" stroke-width="3" fill="none"/>
  <path d="M85,50 L115,50 M55,50 L40,40 M145,50 L160,40" stroke="#333" stroke-width="3" fill="none"/>
  <text x="100" y="80" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#333">SWACHH BHARAT</text>
</svg>"""

# Digital India SVG
digital_india_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="24" fill="#2E3192">Digital India</text>
</svg>"""

# Made in India SVG
made_in_india_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 100">
  <text x="50%" y="40%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="20" fill="#333">Made in</text>
  <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-weight="bold" font-size="28" fill="#FF9933">INDIA</text>
</svg>"""

with open(os.path.join(assets_dir, "make_in_india.svg"), "w") as f:
    f.write(make_in_india_svg)

with open(os.path.join(assets_dir, "swachh_bharat.svg"), "w") as f:
    f.write(swachh_bharat_svg)

with open(os.path.join(assets_dir, "digital_india.svg"), "w") as f:
    f.write(digital_india_svg)

with open(os.path.join(assets_dir, "made_in_india.svg"), "w") as f:
    f.write(made_in_india_svg)

print("Created SVGs.")
