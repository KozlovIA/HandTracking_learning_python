import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()    # success = True/false. if frame is reading



    cv2.imshow("Image", img)
    cv2.waitKey(1)