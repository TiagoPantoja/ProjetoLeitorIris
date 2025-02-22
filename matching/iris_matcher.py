from scipy.spatial.distance import hamming

class IrisMatcher:
    """
    Classe responsável por comparar dois vetores de características de íris
    usando a distância de Hamming.
    """

    def match(self, features1, features2, threshold=0.3):
        """
        Compara dois vetores de características de íris por meio da
        distância de Hamming.

        Args:
            features1 (array-like): Primeiro conjunto de características de íris.
            features2 (array-like): Segundo conjunto de características de íris.
            threshold (float, opcional): Limite máximo de distância para que os
                vetores sejam considerados uma correspondência (match).
                Padrão é 0.3.

        Returns:
            tuple(bool, float): Uma tupla contendo:
                - bool: Indica se os vetores correspondem (True) ou não (False),
                  com base se a distância é menor que o limiar (threshold).
                - float: O valor da distância de Hamming calculada.
        """
        distance = hamming(features1, features2)
        return distance < threshold, distance
