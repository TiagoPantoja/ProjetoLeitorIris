from capture.iris_capture import IrisCapture
from preprocessing.iris_preprocessor import IrisPreprocessor
from feature_extraction.iris_feature_extractor import IrisFeatureExtractor
from matching.iris_matcher import IrisMatcher
from database.in_memory_database import InMemoryDatabase
from models.iris_model import IrisTemplate


class IrisReaderService:
    def __init__(self):
        self.capture = IrisCapture()
        self.preprocessor = IrisPreprocessor()
        self.feature_extractor = IrisFeatureExtractor()
        self.matcher = IrisMatcher()
        self.database = InMemoryDatabase()

    def initialize_camera(self):
        return self.capture.initialize_camera()

    def enroll_user(self, user_id: str):
        image = self.capture.capture_image()
        preprocessed = self.preprocessor.preprocess(image)
        features = self.feature_extractor.extract_features(preprocessed)
        template = IrisTemplate.from_array(user_id, features)
        self.database.add_template(template)
        return f"User {user_id} enrolled successfully"

    def identify_user(self):
        image = self.capture.capture_image()
        preprocessed = self.preprocessor.preprocess(image)
        features = self.feature_extractor.extract_features(preprocessed)

        best_match = None
        best_distance = float('inf')

        for template in self.database.get_all_templates().values():
            match, distance = self.matcher.match(features, template.to_array())
            if match and distance < best_distance:
                best_match = template.user_id
                best_distance = distance

        if best_match:
            return best_match, 1 - best_distance
        else:
            return None, 0

    def release_camera(self):
        self.capture.release()

