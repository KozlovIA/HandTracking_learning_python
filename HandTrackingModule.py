import cv2
import mediapipe as mp
import time

#from mediapipe.python.solutions.hands import HandLandmark

#from mediapipe.python.solutions import hands

class handDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw = True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):       # handNo = 0 or -1
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                #print(id, cx, cy)
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 100, 100), cv2.FILLED)
        return lmList




def main():
    pTime = 0   #previous
    cTime = 0   #current
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()    # success = True/false. if frame is reading
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        lmList_1 = detector.findPosition(img, -1, True)
        #if len(lmList) !=0:
        #    print(lmList[4])
        #if len(lmList_1) !=0:
        #    print(lmList_1[4])
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (25, 240, 10), 2)


        cv2.imshow("Image", img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()