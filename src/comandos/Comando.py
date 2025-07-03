from abc import ABC, abstractmethod

class Comando(ABC):
    """
        Executa o comando.
    """
    @abstractmethod
    def executar(self):
        pass