from PIL import Image

img = Image.open("2.jpg")
area = (100, 100, 300, 300)
cropped_img = img.crop(area)
cropped_img.show()