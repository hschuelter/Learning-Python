import numpy as np
import cv2

def dotCounter(img, color):
	count = 0
	for i in range(0,img.shape[0]):
		for j in range(0, img.shape[1]):
			if img[i][j] == color:
				count += 1

	return count


borderless = cv2.imread('imagens/ruidoBin.png',0)
img = cv2.copyMakeBorder(borderless, 1,1,1,1, cv2.BORDER_CONSTANT, -1)

print dotCounter(img, -1)

cv2.imshow('ruido', img)
cv2.waitKey(0)
cv2.destroyAllWindows()