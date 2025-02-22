from scipy.spatial.distance import hamming

class IrisMatcher:
    def match(self, features1, features2, threshold=0.3):
        distance = hamming(features1, features2)
        return distance < threshold, distance

