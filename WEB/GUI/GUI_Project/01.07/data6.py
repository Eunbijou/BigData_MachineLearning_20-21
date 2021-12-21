import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\Public\\Lena.png', 0)

cv2.imshow('ogrey', image)
cv2.waitKey()
cv2.destroyAllWindows()

grey_i = cv2.equalizeHist(image)

hist, bins = np.histogram(grey_i, 256, [0, 255])

plt.fill_between(range(256), hist, 0)
plt.xlabel('pixel value')
plt.show()

cv2.imshow('eg', grey_i)
cv2.waitKey()
cv2.destroyAllWindows()

color = cv2.imread('C:\\Users\\Public\\Lena.png')
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
color_eq = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('oc', color)
cv2.imshow('eq', color_eq)
cv2.waitKey()
cv2.destroyAllWindows()