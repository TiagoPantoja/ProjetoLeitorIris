import cv2
import numpy as np
from models.iris_model import IrisTemplate


class DataLoader:
    """
    Classe utilitária para carregar e salvar dados relacionados às imagens
    e templates de íris.
    """

    @staticmethod
    def load_image_from_file(file_path: str) -> np.ndarray:
        """
        Carrega uma imagem de um arquivo e retorna em formato de array numpy (BGR).

        Args:
            file_path (str): Caminho completo até o arquivo da imagem.

        Raises:
            ValueError: Se a imagem não puder ser carregada (caminho inválido ou arquivo corrompido).

        Returns:
            np.ndarray: A imagem lida pelo OpenCV em formato BGR.
        """
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Failed to load image from {file_path}")
        return image

    @staticmethod
    def load_template_from_file(file_path: str) -> IrisTemplate:
        """
        Carrega um IrisTemplate de um arquivo .npz (NumPy) previamente salvo.

        Espera-se que o arquivo possua os campos 'user_id' e 'features'.
        Exemplo de uso:
            template = DataLoader.load_template_from_file("template_user123.npz")

        Args:
            file_path (str): Caminho completo até o arquivo .npz.

        Returns:
            IrisTemplate: Instância de IrisTemplate, contendo user_id (str) e features (list).
        """
        # Carrega o dicionário/arquivo npz
        data = np.load(file_path, allow_pickle=True)
        user_id = str(data['user_id'])  # Garante que seja string
        features = data['features']

        # Converte possíveis arrays em lista
        if isinstance(features, np.ndarray):
            features = features.tolist()

        return IrisTemplate(user_id=user_id, features=features)

    @staticmethod
    def save_template_to_file(template: IrisTemplate, file_path: str) -> None:
        """
        Salva um IrisTemplate em formato .npz (NumPy) para posterior carregamento.

        Exemplo de uso:
            DataLoader.save_template_to_file(meu_template, "template_user123.npz")

        Args:
            template (IrisTemplate): Objeto que será salvo, contendo user_id e features.
            file_path (str): Caminho completo para salvar o arquivo .npz.
        """
        # Converte features em array numpy antes de salvar
        features_array = np.array(template.features)
        np.savez(file_path, user_id=template.user_id, features=features_array)
