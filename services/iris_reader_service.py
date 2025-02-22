from capture.iris_capture import IrisCapture
from preprocessing.iris_preprocessor import IrisPreprocessor
from feature_extraction.iris_feature_extractor import IrisFeatureExtractor
from matching.iris_matcher import IrisMatcher
from database.in_memory_database import InMemoryDatabase
from models.iris_model import IrisTemplate

class IrisReaderService:
    """
    Orquestra todo o fluxo de captura de imagem de íris, pré-processamento,
    extração de recursos, comparação/matching e gerenciamento de templates
    (armazenados em um banco de dados em memória).

    Métodos principais:
      - initialize_camera: inicia a câmera.
      - enroll_user: cadastra um novo usuário, armazenando seu template.
      - identify_user: identifica um usuário com base em uma imagem capturada.
      - release_camera: libera o recurso da câmera.
    """

    def __init__(self):
        """
        Inicializa todas as dependências utilizadas no processo:
          - IrisCapture para captura de imagem.
          - IrisPreprocessor para pré-processamento da imagem.
          - IrisFeatureExtractor para extrair as características relevantes.
          - IrisMatcher para comparar duas amostras de íris (matching).
          - InMemoryDatabase para armazenar e recuperar templates de usuários.
        """
        self.capture = IrisCapture()
        self.preprocessor = IrisPreprocessor()
        self.feature_extractor = IrisFeatureExtractor()
        self.matcher = IrisMatcher()
        self.database = InMemoryDatabase()

    def initialize_camera(self) -> bool:
        """
        Inicializa a câmera associada ao índice padrão (geralmente 0).

        Returns:
            bool: True se a câmera foi aberta com sucesso, caso contrário False.
        """
        return self.capture.initialize_camera()

    def enroll_user(self, user_id: str) -> str:
        """
        Captura uma imagem da íris do usuário, pré-processa, extrai as características
        e salva o resultado no banco de dados em memória, associando ao user_id.

        Args:
            user_id (str): O identificador único do usuário.

        Returns:
            str: Uma mensagem confirmando o cadastramento do usuário.
        """
        image = self.capture.capture_image()
        preprocessed = self.preprocessor.preprocess(image)
        features = self.feature_extractor.extract_features(preprocessed)
        template = IrisTemplate.from_array(user_id, features)
        self.database.add_template(template)
        return f"User {user_id} enrolled successfully"

    def identify_user(self) -> tuple[str | None, float]:
        """
        Captura uma imagem para identificação, pré-processa e extrai suas características.
        Em seguida, compara com todos os templates já armazenados no banco de dados,
        buscando o melhor match (caso exista).

        Returns:
            tuple[str | None, float]:
                - best_match (str | None): ID do usuário mais compatível ou None se não encontrado.
                - score (float): Pontuação de similaridade (0 a 1);
                                 quanto mais próximo de 1, maior a probabilidade de correspondência.
        """
        image = self.capture.capture_image()
        preprocessed = self.preprocessor.preprocess(image)
        features = self.feature_extractor.extract_features(preprocessed)

        best_match = None
        best_distance = float('inf')

        # Verifica cada template do banco para encontrar o melhor match.
        for template in self.database.get_all_templates().values():
            match, distance = self.matcher.match(features, template.to_array())
            if match and distance < best_distance:
                best_match = template.user_id
                best_distance = distance

        if best_match is not None:
            # Converte distância em score: quanto menor a distância, maior o score.
            return best_match, 1 - best_distance
        else:
            return None, 0

    def release_camera(self):
        """
        Libera o acesso à câmera, encerrando seu uso.
        """
        self.capture.release()
