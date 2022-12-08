import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import keyboard

detector1 = FaceDetector(minDetectionCon=0.8)  # (minDetectionCon = 0.8)
detector2 = HandDetector(detectionCon=0.8, maxHands=2)

cvSpanMin = 25
cvSpanMax = 900
ardSpanMcvSpanMin = 0
ardSpanMcvSpanMax = 255

# cap = cv2.VideoCapture('http://192.168.137.95:81/stream')

# cap = cv2.VideoCapture("192.168.137.209")

cap = cv2.VideoCapture(0)

if cap.isOpened():
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float

# Calculate Gx and Gy for grid lines
gX = int(w / 2)
gY = int(h / 2)

print(gX, gY)

def mapFromTo(value, cvSpanMin, cvSpanMax, ardSpanMcvSpanMin, ardSpanMcvSpanMax):
    lSpan = cvSpanMax - cvSpanMin
    rSpan = ardSpanMcvSpanMax - ardSpanMcvSpanMin
    valueScaled = float(value - cvSpanMin) / float(lSpan)

    return ardSpanMcvSpanMin + (valueScaled * rSpan)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.line(img, (gX, 0), (gX, gY*2), (0, 255, 0), 5)

    face, bbox = detector1.findFaces(img)
    # print(bbox)

    # hands, img = detector2.findHands(img)  # with draw
    # print(img)


    if len(bbox) != 0:
        face_coordinates_x = bbox[0]["bbox"][0]
        if face_coordinates_x > 400:
            keyboard.press('left')
            keyboard.release('right')
        elif face_coordinates_x < 200:
            keyboard.release('left')
            keyboard.press('right')

        print(bbox[0]["bbox"][0])



    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
