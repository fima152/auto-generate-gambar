from PIL import Image, ImageDraw
from datetime import datetime
import os

os.makedirs("output", exist_ok=True)

img = Image.new("RGB", (1280, 720), color=(20, 28, 58))
draw = ImageDraw.Draw(img)

title = "AUTO GENERATE GAMBAR"
subtitle = datetime.utcnow().strftime("Generated at %Y-%m-%d %H:%M UTC")

draw.text((80, 220), title, fill=(255, 255, 255))
draw.text((80, 320), subtitle, fill=(180, 220, 255))

img.save("output/hasil-gambar.png")
