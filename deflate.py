import PIL
from PIL import Image

mywidth = 1920
myheight = 1080

img = Image.open("input_image.png")

# Convert image to RGB mode
img = img.convert("RGB")

img = img.resize((mywidth, myheight), PIL.Image.LANCZOS)

img.save("resi.png", optimize=True)
