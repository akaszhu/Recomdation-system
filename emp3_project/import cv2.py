import cv2
import numpy as np
import mediapipe as mp


cap =cv2.VideoCapture(0)

while True:
    frm=cap.read()
    cv2.imshow("Window",frm)
    if cv2.waitKey(1)==20:
        cv2.destroyAllWindows()
        cap.release()
        break;