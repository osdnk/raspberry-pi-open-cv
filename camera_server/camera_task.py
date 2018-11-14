import numpy as np
import cv2

# Initialize camera
cap = cv2.capture(0)
while True:
    _, frame = cap.read()
    try:
        cut_frame = frame[0:480, 0:320]
        # cut_frame = frame[self.x_min:self.x_max, self.y_min:self.y_max]
        frame[0:480, 0:320] = frame
        # frame[self.x_min:self.x_max, self.y_min:self.y_max] = frame
        cv2.imwrite("images/snap.png", frame)
    except cv2.error:
        print("Improperly defined resolution bounds or parameter values")
        break
    if cv2.waitKey(30) >= 0:
        break
cap.release()
cv2.destroyAllWindows()