import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import math
import serial_comm

detector1 = FaceDetector(minDetectionCon=0.3)  # (minDetectionCon = 0.8)
detector2 = HandDetector(detectionCon=0.8, maxHands=3)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    face, bbox = detector1.findFaces(img)
    # print(bbox)

    hands, img = detector2.findHands(img)  # with draw
    # print(img)

    if len(bbox) != 0 and len(hands) >= 2:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        hand2 = hands[1]
        lmList2 = hand2["lmList"]  # List of 21 Landmark points
        bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
        centerPoint2 = hand2['center']  # center of the hand cx,cy
        handType2 = hand2["type"]  # Hand Type "Left" or "Right"

        dist = math.dist(centerPoint1, centerPoint2)

        print(dist)
        if dist < 200 and dist > 100:
            serial_comm.send_value_to_arduino(1)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
