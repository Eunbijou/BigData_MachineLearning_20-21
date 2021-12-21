import cv2
import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\Public\\Lena.png', 0).astype(np.float32) / 255

fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(fft, axes=[0, 1])

sz = 25
mask = np.zeros(fft.shape, np.uint8)
mask[image.shape[0]//2 - sz : image.shape[0]//2 + sz, image.shape[1]//2 - sz : image.shpae[1]//2 + sz, :] = 1

shifted *= 1 - mask

fft = np.fft.ifftshift(shifted, axes=[0, 1])
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

plt.figure()
plt.subplot(121)
plt.title('original')
plt.imshow(image, cmap='gray')

plt.subplot(122)
plt.axis('off')
plt.title('no high frequencies')
plt.imshow(filtered, cmap='gray')
plt.tight_layout(True)
plt.show()