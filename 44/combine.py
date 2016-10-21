from PIL import Image

img1 = Image.open("2.jpg")
img2 = Image.open("3.jpg")

area = (50, 50, 1074, 818)
img1.paste(img2, area)

img1.show()