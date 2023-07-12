class Endereco:

    def __init__(self, logradouro, numero, bairro, cidade, sigla):
        self.__logradouro = logradouro
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__sigla = sigla

    @property
    def logradouro(self):
        return self.__logradouro
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def sigla(self):
        return self.__sigla
    
    @logradouro.setter
    def logradouro(self, logradouro):
        self.__logradouro = logradouro

    @numero.setter
    def numero(self, numero):
        self.__numero = numero


    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @sigla.setter
    def sigla(self, sigla):
        self.__sigla = sigla

    def __str__(self):
        return f'{self.__logradouro}, {self.__numero} - {self.__bairro} - {self.__cidade}/{self.__sigla}'  
    