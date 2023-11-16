from PIL import Image

def header(text, symbol):
    print(symbol*20)
    print(text)
    print(symbol*20)
    print()
    return 'welcome to the image data info'

img = Image.open('./../../../ImagescleanPy/src/CamillePissaro1.jpg')

print(header('Image basic data', '='))
print()
print("format: ", img.format)
print("size in pixels: " , img.size)
print("coloring: " , img.mode)

#print(dir(img))



