class MenuPrincipal:

    def __init__(self):
        self.__opcoes = [1, 2, 3]
   
    def selecionar(self):
        print('\n' + '=' * 10 + ' MENU PRINCIPAL ' + '=' * 10 + '\n') 
        opcao = int(input("1 - Conta\n2 - Cliente\n3 - Sair\n\nDigite sua opção: "))
        while opcao not in self.__opcoes:
            print("\nOpção Inválida.\n")
            print('\n' + '=' * 10 + ' MENU PRINCIPAL ' + '=' * 10 + '\n') 
            opcao = int(input("1 - Conta\n2 - Cliente\n3 - Sair\n\nDigite sua opção: "))
        return opcao

class MenuContaCorrente(MenuPrincipal):
    
    def __init__(self):
        self.__opcoes = [1, 2, 3, 4, 5, 6, 7]

    def selecionar(self):
        print('\n' + '=' * 10 + ' MENU CONTA CORRENTE ' + '=' * 10 + '\n') 
        opcao = int(input("1 - Cadastrar nova conta\n2 - Exibir saldo de conta\n" + 
        "3 - Depositar valor em conta\n4 - Sacar valor em conta\n5 - Emitir extrato de conta\n6 - Listar Contas\n7 - Sair\n\nDigite sua opção: "))
        while opcao not in self.__opcoes:
            print("\nOpção Inválida.\n")
            print('\n' + '=' * 10 + ' MENU CONTA CORRENTE ' + '=' * 10 + '\n') 
            opcao = int(input("1 - Cadastrar nova conta\n2 - Exibir saldo de conta\n" + 
        "3 - Depositar valor em conta\n4 - Sacar valor em conta\n5 - Emitir extrato de conta\n6 - Listar Contas\n7 - Sair\n\nDigite sua opção: "))
        return opcao
    
0    
class MenuCliente(MenuPrincipal):

    def __init__(self):
        self.__opcoes = [1, 2, 3, 4, 5, 6]

    def selecionar(self):
        print('\n' + '=' * 10 + ' MENU CLIENTE ' + '=' * 10 + '\n') 
        opcao = int(input("1 - Cadastrar cliente\n2 - Exibir cliente\n" + 
                      "3 - Atualizar cliente\n4 - Excluir cliente\n5 - Listar clientes\n6 - Sair\n\nDigite sua opção: "))
        while opcao not in self.__opcoes:
            print("\nOpção Inválida.\n")
            print('\n' + '=' * 10 + ' MENU CLIENTE ' + '=' * 10 + '\n') 
            opcao = int(input("1 - Cadastrar cliente\n2 - Exibir cliente\n" + 
            "3 - Atualizar cliente\n4 - Excluir cliente\n5 - Listar clientes\n6 - Sair\n\nDigite sua opção: "))
        return opcao
