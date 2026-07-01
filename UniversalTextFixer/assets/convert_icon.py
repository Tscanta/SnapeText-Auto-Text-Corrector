from PIL import Image

img = Image.open("assets/snape_tray_icon_v0.8.ico")

img.save(
    "assets/snape_tray_icon_v0.8.ico",
    format="ICO",
    sizes=[
        (16, 16),
        (24, 24),
        (32, 32),
        (48, 48),
        (64, 64),
        (128, 128),
        (256, 256)
    ]
)

print("Icon created!")