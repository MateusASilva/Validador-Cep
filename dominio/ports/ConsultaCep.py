from abc import ABC, abstractmethod


class ConsultaCep(ABC):

    @abstractmethod
    def consultarCep(self, cep: str):
        pass
