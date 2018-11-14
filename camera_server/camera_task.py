import numpy as np
import cv2

_PATH = '../video_cap/resources/trained_models/haarcascade_frontalface_default.xml'


# Initialize camera
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    try:
        cut_frame = frame[0:480, 0:320]
        # cut_frame = frame[self.x_min:self.x_max, self.y_min:self.y_max]
        frame[0:480, 0:320] = frame
        # frame[self.x_min:self.x_max, self.y_min:self.y_max] = frame
        face_haar_cascade = cv2.CascadeClassifier(_PATH)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_haar_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print("Face detected!!!")
        cv2.imwrite("static/images/snap.png", frame)
    except cv2.error:
        print("Improperly defined resolution bounds or parameter values")
        break
    if cv2.waitKey(600) >= 0:
        break
cap.release()
cv2.destroyAllWindows()