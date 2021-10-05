from infra.service.ConsultaCepService import ConsultaCepService

consultaCep = ConsultaCepService()
cep = consultaCep.consultarCep("teste")
print(cep.getCodigo, " ", cep.getLogradouro)