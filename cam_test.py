import cv2

for i in range(10):
    cap = cv2.VideoCapture(i)
    ret, frame = cap.read()
    if ret:
        print("Camera works at index:", i)
        cv2.imshow(f"Camera {i}", frame)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
    cap.release()