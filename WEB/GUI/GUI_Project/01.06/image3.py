import cv2

def print_capture_properties(*args):
    capture = cv2.VideoCapture(*args)
    print('Created capture', ''.join(map(str, args)))
    print('Frame Count: ', int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
    print('Frame width : ', int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height : ', int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame rate : ', int(capture.get(cv2.CAP_PROP_FPS)))

print_capture_properties('C:\\Users\\Public\\drop.avi')
print_capture_properties(0)
