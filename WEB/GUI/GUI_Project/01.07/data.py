import cv2
import numpy as np

mat = np.random.rand(100, 100).astype(np.float32)
np.savetxt('mat.csv', mat)

mat = np.loadtxt('mat.csv').astype(np.float32)
print('Shape : ', mat.shape)
print('Data Type : ', mat.dtype)