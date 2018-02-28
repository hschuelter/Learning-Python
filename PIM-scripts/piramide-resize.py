import numpy as np
from PIL import Image as im

pic = im.open('triforce.jpg')

x = 200
y = 800

imgSmall = pic.resize((x, x), im.ANTIALIAS)
imgBig = pic.resize((y,y), im.ANTIALIAS)


pic.show()
imgSmall.show()
imgBig.show()