/* Marquee / Infinite Logo Scroll */
.logo-marquee {
    overflow: hidden;
    white-space: nowrap;
    position: relative;
    width: 100%;
    padding: 40px 0;
    background: transparent; /* Or match footer bg */
}

.logo-track {
    display: flex;
    width: max-content; /* Important for fitting all items */
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
    height: 80px; /* Uniform height */
    width: auto;
    object-fit: contain;
    max-width: 150px;
}

@keyframes marquee {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); } /* Move by half the width (one full set) */
}

/* Pause on hover for better UX */
.logo-track:hover {
    animation-play-state: paused;
}
