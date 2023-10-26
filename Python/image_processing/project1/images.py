from PIL import Image, ImageFilter
import os

img = Image.open(os.path.join('G:\portafolio\\12a_DataStructuresAndAlgorithms\Python\image_processing\project1\monetpainting1.jpg'))
img_filter = img.filter(ImageFilter.DETAIL)
img_filter.thumbnail((412, 914))
img_filter.save('thumbnail.jpg')

# filtered_image = img.filter(ImageFilter.DETAIL)
# filtered_image.save("monetdetail.png", 'PNG')

# with Image.open("./project1/monetpainting1.jpg") as im:
#     im.rotate(45).show()    