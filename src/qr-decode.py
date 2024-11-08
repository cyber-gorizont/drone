#!/usr/bin/python3

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    _, frame = cap.read()
    decodeObjects = pyzbar.decode(frame)
    for obj in decodeObjects:
        print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

