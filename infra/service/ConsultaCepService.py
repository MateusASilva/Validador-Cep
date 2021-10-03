from dominio.ports import ConsultaCep
from dominio.model import Cep

class ConsultaCepService(ConsultaCep):
    def consultarCep(self,cep:str):
        return Cep(cep,'Rua Qualquer','Cacupe','Florianopolis','SC')
