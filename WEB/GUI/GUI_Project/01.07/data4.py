import cv2
import numpy as np

image = cv2.imread('C:\\Users\\Public\\Lena.png').astype(np.float32) / 255

image1 = image - image.mean()
image2 = image / image.std()

cv2.imshow('mean', image1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('std', image2)
cv2.waitKey()
cv2.destroyAllWindows()