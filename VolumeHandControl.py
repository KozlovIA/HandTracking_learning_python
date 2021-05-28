import cv2
import time
import numpy as np
import math
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


###############################
wCam, hCam = 640, 480   #640, 480
cTime = 0
pTime = 0
start = False
volBar = 400
volPer = 0
###############################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector()

# lib AndreMiras/pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
Vmin = volume.GetVolumeRange()[0]
Vmax = volume.GetVolumeRange()[1]

while True:
    success, img = cap.read()

    cv2.rectangle(img, (50, 100), (80, 400), (100, 250, 20), 3)
    if start == False:
        cv2.putText(img, "?", (52, 275), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (100, 250, 20), 2)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if(len(lmList) != 0):
        start = True
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (x1, y1), 15, (250, 100, 150), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (250, 100, 150), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (250, 40, 250), 3)
        length = math.hypot(x2 - x1, y2 - y1)
        # Hand range 20 to 250, volume range -37 to 0
        vol = np.interp(length, [20, 250], [Vmin, Vmax])
        volume.SetMasterVolumeLevel(vol, None)
        volBar = np.interp(length, [20, 250], [400, 100])
        volPer = np.interp(vol, [-37, 0], [0, 100])
        if(int(length) >= 250 or int(length) <= 20):
            cv2.circle(img, (cx, cy), 10, (0, 250, 0), cv2.FILLED)
        else:
            cv2.circle(img, (cx, cy), 10, (200, 100, 250), cv2.FILLED)
    cv2.rectangle(img, (50, int(volBar)), (80, 400), (100, 250, 20), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (33, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (150, 250, 20), 3)
    


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (50, 250, 0), 2)
    cv2.imshow("Img", img)
    cv2.waitKey(1)
