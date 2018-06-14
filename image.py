from PIL import Image

basewidth = 300

img = Image.open('Green_tree_python_snake.jpg')

wpercent = (basewidth/float(img.size[0]))

hsize = int((float(img.size[1])*float(wpercent)))

img = img.resize((basewidth,hsize), Image.ANTIALIAS)

img.save('resized.jpg')