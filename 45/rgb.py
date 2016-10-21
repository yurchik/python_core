from PIL import Image
from PIL import ImageFilter

img = Image.open("3.jpg")

r, g, b = img.split()
#
# r.show()
# g.show()
# b.show()
#
# aquare_img = img.resize((500, 500))
# flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
#
# aquare_img.show()
# flip_img.show()
#
# img_black_white = img.convert("L")
#
# img_black_white.show()

blur = img.filter(ImageFilter.BLUR)
detail = img.filter(ImageFilter.DETAIL)

# blur.show()
detail.show()