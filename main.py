import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui


wCam, hCam = 640, 480
frameR = 100
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()
print(wScr, hScr)
smooth = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        #print(x1, x2, y1, y2)

        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255))
        print(fingers)

        if fingers[1] == 1 and fingers[2] == 0:

            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
            clocX = plocX + (x3 - plocX) / smooth
            clocY = plocY + (y3 - plocY) / smooth
            pyautogui.moveTo(wScr - x3, y3)
            cv2.circle(img, (x1, y1), 15, (255, 0, 155),
                       cv2.FILLED)
            plocX, plocY = clocX, clocY

        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
            if length < 40 :
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)
