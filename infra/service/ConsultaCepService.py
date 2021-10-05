from dominio.model.Cep import Cep
from dominio.ports.ConsultaCep import ConsultaCep


class ConsultaCepService(ConsultaCep):
    def consultarCep(self, cep: str):
        return Cep(cep, 'Rua Qualquer', 'Cacupe', 'Florianopolis', 'SC')
