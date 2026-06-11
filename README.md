# ESP32-CAM Object Detection using OpenCV

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![ESP32-CAM](https://img.shields.io/badge/ESP32--CAM-AI%20Thinker-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Project Overview

This project implements a real-time object detection system using an ESP32-CAM and OpenCV's Deep Neural Network (DNN) module. Images are captured by the ESP32-CAM over Wi-Fi and processed using the MobileNet SSD model trained on the COCO dataset.

Detected objects are displayed with bounding boxes and confidence scores in real time.

---

## 🚀 Features

- Real-time object detection
- Wireless image streaming from ESP32-CAM
- MobileNet SSD object recognition
- Bounding box visualization
- Confidence score display
- Lightweight and easy to deploy
- Supports 80+ COCO object classes

---

## 🛠 Hardware Requirements

- ESP32-CAM (AI Thinker)
- FTDI/USB-to-TTL Programmer
- USB Cable
- Wi-Fi Network
- Computer/Laptop

---

## 💻 Software Requirements

- Python 3.x
- OpenCV
- NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

---

## 📂 Project Structure

```text
ESP32-CAM-Object-Detection/
│
├── Object_detection.py
├── coco.names
├── frozen_inference_graph.pb
├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
├── README.md
```

---

## 📥 Required Model Files

Download the following files and place them in the project directory:

### COCO Class Labels
```
coco.names
```

### Model Configuration
```
ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
```

### Pre-trained Weights
```
frozen_inference_graph.pb
```

---

## ⚙️ ESP32-CAM Setup

1. Open Arduino IDE.
2. Install ESP32 board support.
3. Open:

```
File → Examples → ESP32 → Camera → CameraWebServer
```

4. Enter your Wi-Fi credentials.
5. Select **AI Thinker ESP32-CAM**.
6. Upload the sketch.
7. Open Serial Monitor and note the assigned IP address.

Example:

```
192.168.148.110
```

---

## 🔧 Configure Python Script

Update the camera URL:

```python
url = 'http://192.168.148.110/cam-lo.jpg'
```

For higher image quality:

```python
url = 'http://192.168.148.110/cam-hi.jpg'
```

---

## ▶️ Running the Project

Run the Python script:

```bash
python Object_detection.py
```

The application will:

- Connect to ESP32-CAM
- Receive images continuously
- Detect objects
- Draw bounding boxes
- Display results in real time

---

## 🧠 How It Works

### 1. Image Acquisition

The ESP32-CAM captures and serves images via HTTP.

### 2. Image Processing

OpenCV decodes and resizes incoming images.

### 3. Object Detection

MobileNet SSD performs inference on each frame.

### 4. Visualization

Detected objects are displayed with:

- Object Name
- Confidence Score
- Bounding Box

---

## 🎯 Supported Object Classes

Examples include:

- Person
- Bicycle
- Car
- Motorcycle
- Bus
- Dog
- Cat
- Chair
- Bottle
- Laptop
- Cell Phone

and many more from the COCO dataset.

---

## ⌨ Controls

| Key | Function |
|------|----------|
| ESC | Exit Application |

---

## 📸 Sample Output

```
person: 96.5%
chair: 88.3%
bottle: 79.4%
```

Objects are highlighted using green bounding boxes.

---

## 🔮 Future Enhancements

- Real-time video streaming
- FPS monitoring
- Object tracking
- Cloud integration (AWS/Firebase)
- Email/Telegram alerts
- Data logging
- Livestock and goat monitoring
- Custom object training

---

## 🌱 Applications

- Smart Surveillance
- Home Security
- Smart Agriculture
- Livestock Monitoring
- Visitor Detection
- Industrial Monitoring
- IoT Vision Systems

---

## 👨‍💻 Author

**Jeethan M**

Electronics and Communication Engineering Student

Passionate about IoT, Embedded Systems, Computer Vision, AI, and Smart Farming Technologies.

---

## ⭐ Support

If you found this project useful, please consider giving it a **Star ⭐** on GitHub.
