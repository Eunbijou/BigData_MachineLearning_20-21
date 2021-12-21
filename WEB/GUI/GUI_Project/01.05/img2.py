import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='C:\\Users\\Public\\Lena.png', help='Image path.')
parser.add_argument('--out_png', default='C:\\Users\\Public\\Lena_nonesonsil.png', help='무손실 출력')
parser.add_argument('--out_jpg', default="C:\\Users\\Public\\Lena_sonsil.jpeg", help='손실 출력')

params = parser.parse_args()
img = cv2.imread(params.path)

cv2.imwrite(params.out_png, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
saved_img = cv2.imread(params.out_png)
assert saved_img.all() == img.all()

cv2.imwrite(params.out_jpg, img, [cv2.IMWRITE_JPEG_QUALITY, 0])
