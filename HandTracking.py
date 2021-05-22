import cv2
import mediapipe as mp
import time

from mediapipe.python.solutions.hands import HandLandmark

#from mediapipe.python.solutions import hands


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0   #previous
cTime = 0   #current

while True:
    success, img = cap.read()    # success = True/false. if frame is reading
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                cv2.circle(img, (cx, cy), 10, (255, 100, 100), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (25, 240, 10), 2)


    cv2.imshow("Image", img)
    cv2.waitKey(1)