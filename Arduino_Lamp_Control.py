from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import cv2
import numpy as np

arduino = SerialObject()
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.75, maxHands=1)
len = 0

while True:
    _, img = cap.read()
    hand, img = detector.findHands(img)

    if hand:
        lmList = hand[0]['lmList']
        len, info, img = detector.findDistance(lmList[4], lmList[8], img)
        len = int((len//10)*10-30)

        if len < 0: len = 0
        if len > 100: len = 100
        print(len)
        arduino.sendData([len])

    fill = int(np.interp(len,[0,100],[400,150]))
    cv2.rectangle(img, (50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img, (50,fill),(85,400),(0,255,0),cv2.FILLED)
    cv2.putText(img,f'{len} %',(40,100),cv2.FONT_HERSHEY_COMPLEX,1,
                (0,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


