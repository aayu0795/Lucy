import cv2
import time

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read(0)

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ori', frame)

    # Detect features specified in Haar Cascade
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around recognized faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 200), 2)

    # Display the resulting frame
    cv2.imshow('img', frame)

    # Exit the camera view
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
