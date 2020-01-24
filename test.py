import cv2
import time

curr = int(time.time())
video_capture = cv2.VideoCapture(0)

while curr + 25 != int(time.time()):
    ret, frame = video_capture.read(0)
    cv2.flip(frame, 1, frame)
    cv2.imshow('ori', frame)
    cv2.waitKey(5)

cv2.destroyAllWindows()
