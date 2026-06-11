import cv2
import urllib.request
import numpy as np

# Define camera URL
url = 'http://192.168.148.110/cam-lo.jpg'  # Use cam-hi.jpg for higher resolution if supported
winName = 'ESP32 CAMERA'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

# Load class labels from coco.names
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load model configuration and weights
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    try:
        # Read image from ESP32-CAM
        imgResponse = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)

        # Rotate and resize
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        img = cv2.resize(img, (640, 480))  # Increased video dimensions

        # Object detection
        classIds, confs, bbox = net.detect(img, confThreshold=0.5)

        if len(classIds) != 0:
            for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
                label = f'{classNames[classId - 1]}: {confidence * 100:.1f}%'
                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, label, (box[0], box[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Show result
        cv2.imshow(winName, img)

        # Exit on ESC key
        if cv2.waitKey(5) & 0xFF == 27:
            break

    except Exception as e:
        print(f"Error fetching image: {e}")

cv2.destroyAllWindows()
