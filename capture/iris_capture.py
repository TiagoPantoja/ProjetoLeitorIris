import cv2


class IrisCapture:
    """
    Responsável por capturar imagens de uma câmera para fins de leitura de íris.
    """

    def __init__(self):
        """
        Inicializa o objeto IrisCapture e define a câmera como None.
        """
        self.camera = None

    def initialize_camera(self) -> bool:
        """
        Tenta abrir a câmera padrão (índice 0).

        Returns:
            bool: True se a câmera foi aberta com sucesso, False caso contrário.
        """
        self.camera = cv2.VideoCapture(0)
        return self.camera.isOpened()

    def capture_image(self):
        """
        Captura um frame da câmera.

        Raises:
            Exception: Se a câmera não estiver inicializada ou disponível.
            Exception: Se a captura do frame falhar.

        Returns:
            numpy.ndarray: O frame capturado em formato BGR (array do OpenCV).
        """
        if self.camera is None or not self.camera.isOpened():
            raise Exception("Camera is not initialized or available")

        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Failed to capture image")
        return frame

    def release(self):
        """
        Libera o recurso de câmera, caso esteja aberto.
        """
        if self.camera is not None:
            self.camera.release()
