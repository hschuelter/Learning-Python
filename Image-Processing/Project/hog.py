import cv2
import math
import numpy as np
from skimage import feature
from skimage import exposure

def findOcurrence(imageHog, templateHog):
    startV = 0
    endV = imageHog.shape[0] - templateHog.shape[0]
    startH = 0
    endH = imageHog.shape[1] - templateHog.shape[1]
    for i in range(startV, endV):
        for j in range(startH, endH):
            current = imageHog[i:i+templateHog.shape[1], j:j+templateHog.shape[0]]
            if current == templateHog:
                return current

    return None

def generateHOG(imgName):
    roughImage = cv2.imread(imgName, 0)
    image = cv2.resize(roughImage,(roughImage.shape[1]//4, roughImage.shape[0]//4), interpolation = cv2.INTER_CUBIC)

    #norm = square_normalisation(image, 8)

    (H, imageHOG) = feature.hog(norm, orientations=9, pixels_per_cell=(8, 8),
    cells_per_block=(2, 2), transform_sqrt=True, block_norm="L2-Hys",
    visualise=True)
    imageHOG = exposure.rescale_intensity(imageHOG, out_range=(0, 255))
    imageHOG = imageHOG.astype("uint8")

    return imageHOG, image

def square_normalisation(img, num):
    new_img = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    for y in range (img.shape[0]):
        for x in range (img.shape[1]):
            new_img[y][x] = math.sqrt(img[y][x]) * num

    return new_img


def main():
    imageHOG, rough, norm = generateHOG('boruto.jpg')
    #templateHOG = generateHOG('butiful.png')
    #findu = findOcurrence(imageHOG, templateHOG)
    #print(findu==None)

    #normalize

    

    cv2.imwrite('hog-norm-bolt.png', imageHOG)
    #cv2.imwrite('bolt.png', rough)
    #cv2.imshow('Template', templateHOG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
