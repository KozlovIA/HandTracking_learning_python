import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0   #previous
cTime = 0   #current
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()    # success = True/false. if frame is reading
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    lmList_1 = detector.findPosition(img, -1, True)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (25, 240, 10), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)