import cv2

capture = cv2.VideoCapture('C:\\Users\\Public\\drop.avi')
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print('Frame Count :', frame_count)

print('Position : ', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame0', frame)

print('Position : ', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame1', frame)

capture.set(cv2.CAP_PROP_POS_FRAMES, 100)
print('Position : ', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
_, frame = capture.read()
cv2.imshow('frame100', frame)


cv2.waitKey()
cv2.destroyAllWindows()