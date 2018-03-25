import numpy as np
import cv2
#
from Queue import Queue

positions = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]

def colorirBFS(image, label, color, x, y):
    fila = Queue
    fila.put([color, x, y])

    for k in range(0, 8):
        i, j = positions[k]
        if (image[y + j][x + i] == color):


def main():
    img  = cv2.imread('componentes.png', 0)
    label= np.zeros(img.shape, np.uint8)
    img = cv2.copyMakeBorder(img, 1,1,1,1, cv2.BORDER_CONSTANT, -1)

    color = img[1][1]
    colorirBFS(img, label, color, 1, 1)


    cv2.imshow('', img)
    cv2.waitKey(0)

if __name__== "__main__": main()
