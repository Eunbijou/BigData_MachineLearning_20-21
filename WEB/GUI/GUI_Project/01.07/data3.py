import cv2
import numpy as np

image = cv2.imread('C:\\Users\\Public\\Lena.png').astype(np.float32) / 255

gamma = 0.5
c_image = np.power(image, gamma)

cv2.imshow('image', image)
cv2.imshow('correctde_image', c_image)
cv2.waitKey()
cv2.destroyAllWindows()