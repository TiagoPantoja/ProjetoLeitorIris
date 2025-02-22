import numpy as np
from sklearn.decomposition import PCA


class IrisFeatureExtractor:
    """
    Responsável pela extração de características de uma imagem de íris pré-processada,
    utilizando PCA para redução de dimensionalidade.
    """

    def __init__(self, n_components=50):
        """
        Inicializa o extrator de características com PCA.

        Args:
            n_components (int, opcional): Número de componentes principais do PCA.
                                          Padrão é 50.
        """
        self.pca = PCA(n_components=n_components)

    def extract_features(self, preprocessed_image: np.ndarray) -> np.ndarray:
        """
        Extrai características de uma imagem de íris pré-processada usando PCA.

        - Seleciona uma região específica da imagem (linhas e colunas de 200 a 280).
        - Converte a região em um array unidimensional.
        - Aplica PCA para reduzir a dimensionalidade das características.

        Args:
            preprocessed_image (np.ndarray): A imagem de íris já pré-processada.

        Returns:
            np.ndarray: As características extraídas em um array 1D.
        """
        # Seleciona uma área específica (por exemplo, onde está o padrão da íris).
        iris_region = preprocessed_image[200:280, 200:280]

        # Achata a matriz em um array unidimensional.
        flattened = iris_region.flatten()

        # Aplica PCA para extrair recursos (redução de dimensionalidade).
        features = self.pca.fit_transform(flattened.reshape(1, -1))

        # Retorna como um array 1D (por exemplo, [x1, x2, ...]).
        return features.flatten()