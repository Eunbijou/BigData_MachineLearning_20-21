import argparse
import cv2, random, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='C:\\Users\\Public\\Lena.png', help='')
params = parser.parse_args()
image = cv2.imread(params.path)
image_to_show = np.copy(image)

w, h = image.shape[1], image.shape[0]

def rand_pt():
    return (random.randrange(w),
            random.randrange(h))

finish = False

while not finish:

    cv2.imshow("result", image_to_show)
    key = cv2.waitKey(0)

    if key == ord('p'):
        for pt in [rand_pt() for _ in range(10)]:
            cv2.circle(image_to_show, pt, 3, (255, 0, 0), -1)
    elif key == ord('l'):
        cv2.line(image_to_show, rand_pt(), rand_pt(), (0, 255, 0))
    elif key == ord('c'):
        cv2.putText(image_to_show, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    elif key == 27:
        finish = True


# cv2.circle(image, rand_pt(), 40, (255, 0, 0))
# cv2.circle(image, rand_pt(), 5, (255, 0, 0), cv2.FILLED)
# cv2.circle(image, rand_pt(), 40, (255, 0, 0), 2)
# cv2.circle(image, rand_pt(), 40, (255, 0, 0), 2, cv2.LINE_AA)
#
# cv2.line(image, rand_pt(), rand_pt(), (0, 255, 0))
# cv2.line(image, rand_pt(), rand_pt(), (8, 255, 82), 3)
# cv2.line(image, rand_pt(), rand_pt(), (170, 255, 170), 3, cv2.LINE_AA)
#
# cv2.arrowedLine(image, rand_pt(), rand_pt(), (0, 0, 255), 3, cv2.LINE_AA)
#
# cv2.rectangle(image, rand_pt(), rand_pt(), (255, 255, 0), 3)
#
# cv2.ellipse(image, rand_pt(), rand_pt(0.3), random.randrange(360), 0, 360, (255, 255, 0), 3)
#
# cv2.putText(image, 'OpenCV', rand_pt(), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
# cv2.imshow('result', image)
# key = cv2.waitKey(0)