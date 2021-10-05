class Cep:
    __codigo : str
    __logradouro: str
    __bairro: str
    __cidade: str
    __uf: str

    def __init__(self,codigo,logradouro,bairro,cidade,uf):
        self.__codigo = codigo
        self.__logradouro = logradouro
        self.__bairro = bairro
        self.__cidade = cidade
        self.__uf = uf

    def dicionario(self):
        return {'codigo': self.__codigo,
                'logradouro':self.__logradouro,
                'bairro':self.__bairro,
                'cidade':self.__cidade,
                'uf':self.__uf}
    
    @property
    def getCodigo(self):
        return self.__codigo

    @property
    def getLogradouro(self):
        return self.__logradouro
