import cv2


class IrisCapture:
    def __init__(self):
        self.camera = None

    def initialize_camera(self):
        self.camera = cv2.VideoCapture(0)
        return self.camera.isOpened()

    def capture_image(self):
        if self.camera is None or not self.camera.isOpened():
            raise Exception("Camera is not initialized or available")

        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Failed to capture image")
        return frame

    def release(self):
        if self.camera is not None:
            self.camera.release()
