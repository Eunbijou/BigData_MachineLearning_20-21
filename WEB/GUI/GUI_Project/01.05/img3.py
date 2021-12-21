import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='C:\\Users\\Public\\Lena.png', help='Image path.')
parser.add_argument('--iter', default='50', help='sampling')

params = parser.parse_args()
img = cv2.imread(params.path)
img_size = img.shape[0:2]

cv2.imshow('original image', img)
cv2.waitKey(2000)