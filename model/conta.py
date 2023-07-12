class ContaCorrente:

    LIMITE_SAQUES = 3
    LIMITE = 500
    numero = 0
    transacoes = []

    def __init__(self, agencia, cliente):
        ContaCorrente.numero += 1
        self.__agencia = agencia
        self.__numero = ContaCorrente.numero
        self.__saldo = 0.0
        self.__quantidade = 0
        self.__cliente = cliente

    @property
    def agencia(self):
        return self.__agencia

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def cliente(self):
        return self.__cliente
    
    def validar_valor(self, valor):
        if valor > 0:
            return True
        return False    
    
    def validar_saque(self, valor):
        if valor <= self.__saldo:
            return True
        return False 
    
    def validar_limite(self, valor):
        if valor <= ContaCorrente.LIMITE:
            return True
        return False
    
    def validar_quantidade(self):
        if self.__quantidade < ContaCorrente.LIMITE_SAQUES:
            return True
        return False

    def depositar(self, valor):
        ContaCorrente.transacoes.append(('Depósito', valor))
        self.__saldo += valor

    def sacar(self, valor):
        ContaCorrente.transacoes.append(('Saque', valor))
        self.__saldo -= valor
        self.__quantidade += 1

    def extrato(self):
        print(self.__str__())
        print('\n====================== EXTRATO ======================\n')
        if len(ContaCorrente.transacoes) > 0:
            for transacao in ContaCorrente.transacoes:
                print(f'{transacao[0]}: R$ {transacao[1]:.2f}')
        else:
            print('\nNão foram efetuadas nenhuma movimentação nesta conta.\n')
        print(f'\nSaldo atual: R$ {self.saldo:.2f}')
        print('\n=====================================================\n')   

    def __str__(self):
        return f'\nAgência: {self.agencia}\nConta: {self.__numero}\nSaldo: {self.saldo}{self.cliente}\n'
            