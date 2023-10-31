from PIL import Image, ImageFilter
import os, sys

#JPG to PNG converter

#grab arguments from command line
root= 'G:\portafolio\\12a_DataStructuresAndAlgorithms\Python\image_processing' + '\\'
initial_folder_name = sys.argv[1]
initial_folder = root + initial_folder_name 
new_folder_name = sys.argv[2]
new_folder = root + new_folder_name

#check if new folder exists
if not os.path.exists('new_folder'):
    os.makedirs(new_folder)

#loop through initial folder
for filename in os.listdir(initial_folder):
    img = Image.open(f'{initial_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    filtered_image = img.filter(ImageFilter.DETAIL)
    filtered_image.save(f'{new_folder}{clean_name}.png', 'PNG')
    print("all done")


# img = Image.open(os.path.join('G:\portafolio\\12a_DataStructuresAndAlgorithms\Python\image_processing\project1\monetpainting1.jpg'))



#print(img.size)
# img_filter = img.filter(ImageFilter.DETAIL)
# img_filter.thumbnail((400, 851))
# img_filter.save('thumbnail.jpg')

# filtered_image = img.filter(ImageFilter.DETAIL)
# filtered_image.save("monetdetail.png", 'PNG')

# with Image.open("./project1/monetpainting1.jpg") as im:
#     im.rotate(45).show()    