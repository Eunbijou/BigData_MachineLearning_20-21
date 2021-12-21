import cv2

capture = cv2.VideoCapture(0)
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

video = cv2.VideoWriter('C:\\Users\\Public\\captured_video.mp4', cv2.VideoWriter_fourcc(*'MP4V'),
                        25, (frame_width, frame_height))

while True:
    has_frame, frame = capture.read()
    if not has_frame:
        print('Cant get frame')
        break

    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)

    if key == 27:
        print('Pressed ESC')
        break

capture.realease()
video.release()
cv2.destroyAllWindows()