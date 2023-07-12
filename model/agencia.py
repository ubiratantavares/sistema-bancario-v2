class Agencia:

    numero = '0001'

    def __init__(self):
        self.__contas = []
        self.__clientes = []

    @property
    def contas(self):
        return self.__contas
    
    @property
    def clientes(self):
        return self.__clientes
    
    def total_de_clientes(self):
        return len(self.clientes)
    
    def total_de_contas(self):
        return len(self.contas)

    def pesquisar_cliente_por_cpf(self, cpf):
        if self.total_de_clientes() > 0:
            for posicao in range(0, self.total_de_clientes()):
                cliente = self.clientes[posicao]
                if cliente.cpf == cpf:
                    return cliente
        return None     

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def exibir_cliente(self, cpf):
        pass

    def atualizar_cliente(self, posicao, cliente):
        self.clientes[posicao] = cliente

    def atualizar_conta(self, posicao, conta):
        self.contas[posicao] = conta

    def excluir_cliente(self, cpf):
        pass

    def listar_clientes(self):
        if self.total_de_clientes() > 0:
            for cliente in self.clientes:
                print(cliente)
        else:
            print('Não há clientes cadastrados.')

    def verificar_posicao_cliente(self, cliente):
        return self.clientes.index(cliente)
    
    def verificar_posicao_conta(self, conta):
        return self.contas.index(conta)
    
    def cadastrar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        if self.total_de_contas() > 0:
            for conta in self.contas:
                print(conta)
        else:
            print('Não há contas cadastradas.')

    def pesquisar_conta_por_numero(self, numero):
        if self.total_de_contas() > 0:
            for posicao in range(0, self.total_de_contas()):
                conta = self.contas[posicao]
                if conta.get_numero() == numero:
                    return conta
        return None  
    
