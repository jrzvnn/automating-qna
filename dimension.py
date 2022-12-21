# import required module
from PIL import Image

# get image
filepath = "geeksforgeeks.png"
img = Image.open('test.png')

# get width and height
width = img.width
height = img.height

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)