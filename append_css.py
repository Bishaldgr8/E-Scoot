
css_content = """
/* Marquee / Infinite Logo Scroll */
.logo-marquee {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    width: 100%;
    padding: 40px 0;
    /* background: transparent; */
}

.logo-track {
    display: flex;
    width: max-content;
    animation: marquee 20s linear infinite;
}

.logo-item {
    flex: 0 0 auto;
    margin: 0 40px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.logo-item img {
    height: 80px; 
    width: auto;
    object-fit: contain;
    max-width: 150px;
}

@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); } 
}

.logo-track:hover {
    animation-play-state: paused;
}
"""

with open(r"c:\Users\assdr\Desktop\New Project\custom.css", "a", encoding="utf-8") as f:
    f.write(css_content)
    print("Appended CSS.")
