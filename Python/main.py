import urllib

import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import math
import serial_comm

detector1 = FaceDetector(minDetectionCon=0.8)  # (minDetectionCon = 0.8)
detector2 = HandDetector(detectionCon=0.8, maxHands=3)

cvSpanMin = 25
cvSpanMax = 900
ardSpanMcvSpanMin = 0
ardSpanMcvSpanMax = 255

cap = cv2.VideoCapture('http://192.168.137.166:81/stream')

# cap = cv2.VideoCapture("192.168.137.209")

# cap = cv2.VideoCapture(0)


def mapFromTo(value, cvSpanMin, cvSpanMax, ardSpanMcvSpanMin, ardSpanMcvSpanMax):
    lSpan = cvSpanMax - cvSpanMin
    rSpan = ardSpanMcvSpanMax - ardSpanMcvSpanMin
    valueScaled = float(value - cvSpanMin) / float(lSpan)

    return ardSpanMcvSpanMin + (valueScaled * rSpan)

while True:
    success, img = cap.read()

    face, bbox = detector1.findFaces(img)
    # print(bbox)

    hands, img = detector2.findHands(img)  # with draw
    # print(img)

    if len(bbox) != 0 and len(hands) >= 2:
        # Hand 1
        hand1 = hands[0]
        # lmList1 = hand1["lmList"]  # List of 21 Landmark points
        # bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        # handType1 = hand1["type"]  # Handtype Left or Right
        #
        hand2 = hands[1]
        # lmList2 = hand2["lmList"]  # List of 21 Landmark points
        # bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
        centerPoint2 = hand2['center']  # center of the hand cx,cy
        # handType2 = hand2["type"]  # Hand Type "Left" or "Right"

        dist = math.dist(centerPoint1, centerPoint2)

        print(f"Dist = {dist}")
        if dist < cvSpanMax and dist > cvSpanMin:
            valToSend = mapFromTo(dist, cvSpanMin, cvSpanMax, ardSpanMcvSpanMin, ardSpanMcvSpanMax)
            serial_comm.send_value_to_arduino(valToSend)
            # print(f"valToSend = {valToSend}")
    if len(bbox) <= 0:
        serial_comm.send_value_to_arduino(0)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
