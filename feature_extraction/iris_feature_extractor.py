import numpy as np
from sklearn.decomposition import PCA


class IrisFeatureExtractor:
    def __init__(self, n_components=50):
        self.pca = PCA(n_components=n_components)

    def extract_features(self, preprocessed_image):
        iris_region = preprocessed_image[200:280, 200:280]
        flattened = iris_region.flatten()
        features = self.pca.fit_transform(flattened.reshape(1, -1))
        return features.flatten()
