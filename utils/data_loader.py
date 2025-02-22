import cv2
import numpy as np
from models.iris_model import IrisTemplate

class DataLoader:
    @staticmethod
    def load_image_from_file(file_path: str) -> np.ndarray:
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Failed to load image from {file_path}")
        return image

    @staticmethod
    def load_template_from_file(file_path: str) -> IrisTemplate:
        # This is a placeholder. In a real application, you'd implement
        # a proper serialization/deserialization method for IrisTemplate
        data = np.load(file_path)
        return IrisTemplate(user_id=data['user_id'], features=data['features'].tolist())

    @staticmethod
    def save_template_to_file(template: IrisTemplate, file_path: str):
        # This is a placeholder. In a real application, you'd implement
        # a proper serialization/deserialization method for IrisTemplate
        np.savez(file_path, user_id=template.user_id, features=np.array(template.features))

