from view.menu import *
from model.conta import ContaCorrente
from model.cliente import Cliente
from model.endereco import Endereco
from model.agencia import Agencia

class Main:

    def ler_cpf(self):
        cpf = input('\nDigite o CPF (somente números): ')
        return cpf
    
    def ler_numero_da_conta(self):
        numero = int(input('\nDigite o número da conta corrente: '))
        return numero
    
    def ler_valor(self):
        valor = float(input('\nDigite o valor: '))
        return valor
    
    def existe_cliente(self, cpf, agencia):
        cliente = agencia.pesquisar_cliente_por_cpf(cpf)
        if cliente:
            return True
        return False
    
    def existe_conta(self, numero, agencia):
        conta = agencia.pesquisar_conta_por_numero(numero)
        if conta:
            return True
        return False
    
    def criar_cliente(self, cpf):
        nome = input('\nDigite o nome: ')
        data_nascimento = input('\nDigite a data de nascimento (dd-mm-aaaa): ')
        logradouro = input('\nDigite o logradouro: ')
        numero = input('\nDigite o número: ')
        bairro = input('\nDigite o bairro: ')
        cidade = input('\nDigite a cidade: ')
        sigla = input('\nDigite a sigla do Estado: ')
        endereco = Endereco(logradouro, numero, bairro, cidade, sigla)
        cliente = Cliente(cpf, nome, data_nascimento, endereco)
        return cliente
    
    def criar_conta(self, cliente):
        agencia = Agencia.numero
        conta = ContaCorrente(agencia, cliente)
        return conta
    
    def editar_cliente(self, cliente):
        print('\nInforme os dados atualizados do cliente\n')
        cliente.nome = input('Nome: ')
        cliente.data = input('Data de nascimento (dd-mm-aaaa): ')
        endereco = cliente.endereco
        endereco.logradouro = input('Logradouro: ')
        endereco.numero = input('Número: ')
        endereco.bairro = input('Bairro: ')
        endereco.cidade = input('Cidade: ')
        endereco.sigla = input('Estado (Sigla): ')
        cliente.endereco = endereco
        return cliente

    def cadastrar_dados_de_cliente(self, agencia):
        cpf = self.ler_cpf()
        if self.existe_cliente(cpf, agencia):
            print('\nCliente já cadastrado.\n')  
        else:
            cliente = self.criar_cliente(cpf)
            agencia.cadastrar_cliente(cliente)
            print('\nCliente cadastrado com sucesso.\n')     

    def exibir_dados_de_cliente(self, agencia):
        cpf = self.ler_cpf()
        if self.existe_cliente(cpf, agencia):
            cliente = agencia.pesquisar_cliente_por_cpf(cpf)
            print(cliente)
        else:
            print('\nCPF não cadastrado.\n')

    def atualizar_dados_de_cliente(self, agencia):
        cpf = self.ler_cpf()
        if self.existe_cliente(cpf, agencia):
            cliente = agencia.pesquisar_cliente_por_cpf(cpf) 
            cliente = self.editar_cliente(cliente)
            posicao = agencia.verificar_posicao_cliente(cliente)
            agencia.atualizar_cliente(posicao, cliente)
            print("\nCliente atualizado com sucesso.\n")
        else:
            print('\nCliente não encontrado.\n')       

    def excluir_dados_de_cliente(self, agencia):
        cpf = self.ler_cpf()
        if self.existe_cliente(cpf, agencia):
            cliente = agencia.pesquisar_cliente_por_cpf(cpf) 
            agencia.clientes.remove(cliente)
            print("\nCliente excluído com sucesso.\n")
        else:
            print('\nCliente não encontrado.\n')    

    def listar_dados_de_todos_clientes(self, agencia):
        agencia.listar_clientes() 

    def cadastrar_dados_de_conta(self, agencia):
        cpf = self.ler_cpf()
        cliente = None
        if self.existe_cliente(cpf, agencia):
            cliente = agencia.pesquisar_cliente_por_cpf(cpf) 
        else:
            cliente = self.criar_cliente(cpf)
            agencia.cadastrar_cliente(cliente)
            print('\nCliente cadastrado com sucesso.\n')           
        conta = self.criar_conta(cliente)
        agencia.cadastrar_conta(conta)
        print('\nConta cadastrada com sucesso.\n')  

    def exibir_saldo_da_conta(self, agencia):
        numero = self.ler_numero_da_conta()
        if self.existe_conta(numero, agencia):
            conta = agencia.pesquisar_conta_por_numero(numero)
            print(f'\nSaldo: R$ {conta.saldo:.2f}\n')
        else:
            print('\nConta inexistente.\n')

    def depositar_em_conta(self, agencia):
        numero = self.ler_numero_da_conta()
        if self.existe_conta(numero, agencia):
            conta = agencia.pesquisar_conta_por_numero(numero)
            valor = self.ler_valor()
            if not conta.validar_valor(valor):
                print('\nOperação cancelada. O valor informado é inválido.\n')
            else:
                conta.depositar(valor)
                print('\nDepósito realizado com sucesso.\n')
                posicao = agencia.verificar_posicao_conta(conta)
                agencia.atualizar_conta(posicao, conta)
        else:
            print('\nConta inexistente.\n') 

    def sacar_de_conta(self, agencia):
        numero = self.ler_numero_da_conta()
        if self.existe_conta(numero, agencia):
            conta = agencia.pesquisar_conta_por_numero(numero)
            valor = self.ler_valor()
            if not conta.validar_valor(valor):
                print('\nOperação cancelada. O valor informado é inválido.')
            elif not conta.validar_saque(valor):
                print('\nOperação cancelada. Saldo insuficiente para efetuar o saque.')
            elif not conta.validar_limite(valor):
                print('\nOperação cancelada. O valor informado excede o valor máximo de R$ {:.2f}.'.format(ContaCorrente.LIMITE))
            elif not conta.validar_quantidade():
                print('\nOperação cancelada. A quantidade de saques excede o número máximo permitido por dia.')
            else:
                conta.sacar(valor)
                print('\nSaque realizado com sucesso.')
                posicao = agencia.verificar_posicao_conta(conta)
                agencia.atualizar_conta(posicao, conta)

    def emitir_extrato_de_conta(self, agencia):
        numero = self.ler_numero_da_conta()
        if self.existe_conta(numero, agencia):
            conta = agencia.pesquisar_conta_por_numero(numero)
            conta.extrato()
        else:
            print('\nConta inexistente.\n')   

    def listar_dados_de_todas_contas(self, agencia):
        agencia.listar_contas()

    def executar_opcoes_menu_conta_corrente(self, agencia):
        mcc = MenuContaCorrente()
        while True:
            opcao = mcc.selecionar()
            if opcao == 1:
                self.cadastrar_dados_de_conta(agencia)
            elif opcao == 2:
                self.exibir_saldo_da_conta(agencia)
            elif opcao == 3:
                self.depositar_em_conta(agencia)
            elif opcao == 4:
                self.sacar_de_conta(agencia)
            elif opcao == 5:
                self.emitir_extrato_de_conta(agencia)
            elif opcao == 6:
                self.listar_dados_de_todas_contas(agencia)
            else:
                break

    def executar_opcoes_menu_cliente(self, agencia):
        mc = MenuCliente()
        while True:
            opcao = mc.selecionar()
            if opcao == 1:
                 self.cadastrar_dados_de_cliente(agencia)
            elif opcao == 2:
                self.exibir_dados_de_cliente(agencia)
            elif opcao == 3:
                self.atualizar_dados_de_cliente(agencia)
            elif opcao == 4:
                self.excluir_dados_de_cliente(agencia)
            elif opcao == 5:
                self.listar_dados_de_todos_clientes(agencia)
            else:
                break           

    def executar_opcoes_menu_principal(self, agencia):
        mp = MenuPrincipal()
        while True:
            opcao = mp.selecionar()
            if  opcao == 1:
                self.executar_opcoes_menu_conta_corrente(agencia)
            elif opcao == 2:
                self.executar_opcoes_menu_cliente(agencia)
            else: 
                break
        
if __name__ == "__main__":
    main = Main()
    agencia = Agencia()
    main.executar_opcoes_menu_principal(agencia)
