import cv2


class IrisPreprocessor:
    """
    Responsável pelo pré-processamento de imagens de íris,
    aplicando conversão para escala de cinza, equalização de histograma
    e suavização (blur).
    """

    def preprocess(self, image):
        """
        Executa a pipeline de pré-processamento na imagem fornecida.

        Passos:
          1. Converte para escala de cinza (BGR -> Gray).
          2. Equaliza o histograma para melhorar o contraste.
          3. Aplica um filtro Gaussiano (blur) para suavizar ruídos.

        Args:
            image (numpy.ndarray): A imagem de íris em formato BGR (OpenCV).

        Returns:
            numpy.ndarray: A imagem pré-processada, em escala de cinza e suavizada.
        """
        # Converte para escala de cinza
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Equaliza o histograma
        equalized = cv2.equalizeHist(gray)

        # Aplica o blur Gaussiano
        blurred = cv2.GaussianBlur(equalized, (5, 5), 0)

        return blurred
