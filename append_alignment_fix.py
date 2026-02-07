
css_fix = """
/* Fix for DEVELOPMENT OF E SCOOT FOUNDERS text alignment */
h3.light {
    text-align: left !important;
    word-wrap: break-word;
    white-space: normal;
    max-width: 100%;
}
"""

with open(r"c:\Users\assdr\Desktop\New Project\custom.css", "a", encoding="utf-8") as f:
    f.write(css_fix)
    print("Appended alignment fix CSS.")
