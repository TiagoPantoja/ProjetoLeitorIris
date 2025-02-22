from models.iris_model import IrisTemplate


class InMemoryDatabase:
    """
    Banco de dados simples em memória para armazenar modelos de íris (IrisTemplate).
    As chaves são user_ids (strings), e os valores são instâncias de IrisTemplate.
    """

    def __init__(self):
        """
        Inicializa o dicionário interno que armazena os templates.
        """
        self.templates: dict[str, IrisTemplate] = {}

    def add_template(self, template: IrisTemplate):
        """
        Adiciona um novo template ou atualiza um existente no banco de dados.

        Args:
            template (IrisTemplate): O template de íris a ser armazenado.
        """
        self.templates[template.user_id] = template

    def get_template(self, user_id: str) -> IrisTemplate | None:
        """
        Recupera o template de íris associado a um 'user_id'.

        Args:
            user_id (str): Identificador único do usuário.

        Returns:
            IrisTemplate | None: O template de íris se encontrado, ou None se não existir.
        """
        return self.templates.get(user_id)

    def get_all_templates(self) -> dict[str, IrisTemplate]:
        """
        Retorna todos os templates armazenados no banco de dados em memória.

        Returns:
            dict[str, IrisTemplate]: Dicionário com todos os IrisTemplates (chaveados por user_id).
        """
        return self.templates
