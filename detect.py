import cv2
import numpy as np

# Settings
winName = 'Webcam Object Detection'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

# Load class names
classNames = []

with open('coco.names', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load model
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)

net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Start video capture from webcam
cap = cv2.VideoCapture(0)   # Change 0 to 1 or 2 if needed

while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame")
        break

    classIds, confs, bbox = net.detect(img, confThreshold=0.5)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

            cv2.rectangle(img, box, color=(0, 255, 0), thickness=3)

            cv2.putText(
                img,
                classNames[classId - 1],
                (box[0] + 10, box[1] + 30),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.imshow(winName, img)

    tecla = cv2.waitKey(1) & 0xFF

    if tecla == 27:   # ESC key
        break

cap.release()
cv2.destroyAllWindows()