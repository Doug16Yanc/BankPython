# Projeto de sistema bancário simples para bootcamp Python AI Developer Backend
# Será colocado no repositório numa branche "main"

import sys

def main():

    usuario = "Douglas"
    senha = "1609"
    valorNaConta = 0.0

    print("Entre com seu usuário e senha.\n")

    usuarioValido = input("Usuário : ")
    senhaValida = input("Senha : ")

    if (usuario == usuarioValido and senha == senhaValida):

        while True:
            print(f"Bem-vindo ao seu menu de opções deste extraordinário sistema bancário, caríssimo {usuario}.\n")
            opcao = int(input("Escolha uma opção para realizar:\n" + 
                            "0 - Sair\n"
                            "1 - Depositar\n" +
                            "2 - Sacar\n" +
                            "3 - Obter extrato\n"))
            if opcao == 0:
                print(f"Sua despedida é sempre tão dolorosa, caro {usuario}. Espero te ver logo.\n")
                sys.exit()
            elif opcao == 1:
                deposito = float(input("Digite, em reais, a quantidade que desejas depositar.\n"))
                valorNaConta += deposito
                print(f"Depósito de R$ {deposito} realizado com sucesso.\n")
            elif opcao == 2:
                saque = float(input("Digite, em reais, a quantidade que desejas sacar.\n"))
                if saque <= valorNaConta:
                    print(f"Saque de R$ {saque} realizado com sucesso.\n")
                    valorNaConta -= saque
                else :
                    print("Você não possui saldo suficiente para realizar tal saque.\n")
            elif opcao == 3:
                print(f"Nome do usuário : {usuario}\n" +
                      f"Saldo atual : R$ {valorNaConta}")
            else :
                print("Opção impossível.Por favor, escolha uma que seja possível.\n")
    else:
        print("Credencias não reconhecidas. Encerrando o programa.\n")
        sys.exit()

if __name__ == "__main__":
    main()