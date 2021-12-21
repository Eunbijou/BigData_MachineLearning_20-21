import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\Public\\Lena.png', 0)

cv2.imshow('ogrey', image)
cv2.waitKey()
cv2.destroyAllWindows()

hist, bins = np.histogram(image, 256, [0, 255])

plt.fill(hist)
plt.xlabel('pixel value')
plt.show()