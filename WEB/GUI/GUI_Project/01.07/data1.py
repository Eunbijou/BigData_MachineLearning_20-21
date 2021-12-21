import cv2
import numpy as np

image = cv2.imread('C:\\Users\\Public\\Lena.png').astype(np.float32) / 255
print('Shape : ', image.shape)

image[:, :, [0, 2]] = image[:, :, [2, 0]]
cv2.imshow('Blue_and_Red_Swapped', image)
cv2.waitKey()
cv2.destroyAllWindows()

image[:, :, [0, 2]] = image[:, :, [2, 0]]
image[:, :, 0] = (image[:, :, 0]*0.9).clip(0, 1)
image[:, :, 1] = (image[:, :, 1]*1.1).clip(0, 1)
cv2.imshow('Image', image)
cv2.waitKey()
cv2.destroyAllWindows()