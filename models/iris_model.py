from pydantic import BaseModel
import numpy as np


class IrisTemplate(BaseModel):
    """
    Representa um template de íris, contendo o ID do usuário e
    um conjunto de características (features) para identificação.

    A classe herda de BaseModel (Pydantic), o que permite validação
    automática de tipos e serialização, além de facilidades como métodos
    de criação via dicionários ou JSON.
    """

    user_id: str
    features: list

    class Config:
        """
        Configurações adicionais do modelo Pydantic.

        'arbitrary_types_allowed' permite o uso de tipos que não são
        nativamente suportados pelo Pydantic, como numpy arrays.
        """
        arbitrary_types_allowed = True

    @classmethod
    def from_array(cls, user_id: str, features: np.ndarray):
        """
        Cria uma instância de IrisTemplate a partir de um array numpy.

        Args:
            user_id (str): Identificador do usuário.
            features (np.ndarray): Array numpy que contém as características da íris.

        Returns:
            IrisTemplate: Instância de IrisTemplate com as características convertidas para lista.
        """
        return cls(user_id=user_id, features=features.tolist())

    def to_array(self) -> np.ndarray:
        """
        Converte as características de lista para um array numpy.

        Returns:
            np.ndarray: Array numpy contendo as características da íris.
        """
        return np.array(self.features)
