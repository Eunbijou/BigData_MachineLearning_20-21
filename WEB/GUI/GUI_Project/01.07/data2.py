import cv2
import numpy as np

image = cv2.imread('C:\\Users\\Public\\Lena.png').astype(np.float32) / 255
print('Shape : ', image.shape)
print('Data Type : ', image.dtype)

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Converted to grayscale')
print('Shape : ', gray.shape)
print('Data Type : ', gray.dtype)

cv2.imshow('gray', gray)
cv2.waitKey()
cv2.destroyAllWindows()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print('Converted to hsv')
print('Shape : ', hsv.shape)
print('Data Type : ', hsv.dtype)

cv2.imshow('hsv', hsv)
cv2.waitKey()
cv2.destroyAllWindows()

hsv[:, :, 2] *= 2
from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
print('Converted back to BGR from HSV')
print('Shape : ', from_hsv.shape)
print('Data Type : ', from_hsv.dtype)

cv2.imshow('from_hsv', from_hsv)
cv2.waitKey()
cv2.destroyAllWindows()