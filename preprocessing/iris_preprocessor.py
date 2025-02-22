import cv2

class IrisPreprocessor:
    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        blurred = cv2.GaussianBlur(equalized, (5, 5), 0)
        return blurred

