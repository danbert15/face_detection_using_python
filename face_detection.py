import cv2

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap =cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
