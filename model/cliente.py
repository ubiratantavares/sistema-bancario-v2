class Cliente:

    def __init__(self, cpf, nome, data, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__data = data
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def data(self):
        return self.__data
    
    @property
    def endereco(self):
        return self.__endereco    
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data.setter
    def data(self, data):
        self.__data = data

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    def __str__(self):
        return f'\nCliente: {self.__nome}\nCPF: {self.__cpf}\nData de Nascimento: {self.__data}\nEndereço: {self.__endereco}\n'