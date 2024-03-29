import sys

def iniciar_interacao(usuarios, contas):
    while True :
        print("Olá, caríssimo usuário.\n")
        resposta = input("já é cadastrado em nossa plataforma?\n S/s - Sim \n N/n - Não\n O/o - Sair\n")

        if resposta.lower() == 'n':
            cadastra_usuario(usuarios)
        elif resposta.lower() == 's':
            faz_login(usuarios, contas)
        elif resposta.lower() == 'o':
            sys.exit()
        else:
            print("Opção impossível.\n")
            sys.exit()


    return resposta

def cadastra_usuario(usuarios):
    nome = input("Nome : ")
    cpf = input("Cadastro de pessoa física : ")
    endereco = input("Digite o endereço : ")
    senha = input("Senha para acesso ao sistema : ")

    usuarios.append({"nome": nome, "cpf": cpf, "endereco": endereco, "senha": senha})


def faz_login(usuarios, contas):
    print("Entre com seu CPF e senha:")
    cpf = input("CPF : ")
    senha = input("Senha : ")

    usuario_Validado = valida_usuario(usuarios, cpf, senha)

    if usuario_Validado is not None:
        print("Login realizado com sucesso.\n")
        interage_usuario(usuario_Validado, contas)
    else:
        print("Credenciais não reconhecidas.\n")
        return None

def valida_usuario(usuarios, cpf, senha):
    for usuario in usuarios:
        if usuario["cpf"] == cpf and usuario["senha"] == senha:
            return usuario
    return None

def visualizar_dados(usuario):
    print("Dados do usuário: \n")
    print(f"Nome: {usuario['nome']}\n" +
          f"CPF: {usuario['cpf']}\n" +
          f"Endereço: {usuario['endereco']}")

def interage_usuario(usuario, contas):
    saiu = False
    while True:
        print(f"Bem-vindo(a) ao seu menu de opções deste extraordinário sistema bancário, caríssimo(a) {usuario['nome']}.\n")
        opcao = int(input("Escolha uma opção para realizar:\n" +
                          "0 - Sair\n" +
                          "1 - Criar conta\n" +
                          "2 - Ir para a conta\n" +
                          "3 - Visualizar dados\n" +
                          "4 - Remover conta\n"))

        if opcao == 0:
            print(f"Sua despedida é sempre tão dolorosa, caro {usuario['nome']}. Espero te ver logo.\n")
            saiu = True
            break
        elif opcao == 1:
            criar_conta(usuario, contas)
        elif opcao == 2:
            interage_conta(usuario, contas)
        elif opcao == 3:
            visualizar_dados(usuario)
        elif opcao == 4:
            remover_conta(usuario, contas)
        else:
            print("Opção impossível. Por favor, escolha uma que seja possível.\n")

    if saiu :
        return

def criar_conta(usuario, contas):
    agencia = input("Agência : ")
    numero_conta = input("Número da conta : ")
    saldo_atual = 0.0

    contas.append({"usuario": usuario, "agencia": agencia, "numero_conta": numero_conta, "saldo_atual": saldo_atual})

def valida_conta(usuarios, contas, numero_conta):
    for conta in contas:
        if conta["usuario"] == usuarios and conta["numero_conta"] == numero_conta:
            return conta
    print("Conta não encontrada.\n")
    return None

def interage_conta(usuario, contas):
    numero_conta = input("Digite o número da conta: ")
    conta = valida_conta(usuario, contas, numero_conta)

    if conta is not None:
        oferta_opcoes_conta(conta)
    else:
        print("Conta não encontrada.\n")

def oferta_opcoes_conta(conta):
    print("Selecione uma opção.\n")
    opcao = int(input("\n1 - Realizar depósito : " +
                      "\n2 - Realizar saque : " +
                      "\n3 - Obter extrato : "))
                          
    if opcao == 1:
        realizar_deposito(conta)
    elif opcao == 2:
        realizar_saque(conta)
    elif opcao == 3:
        obter_extrato(conta)
    else:
        print("Opção impossível.\n")

def realizar_deposito(conta):
    deposito = float(input("Digite, em reais, a quantidade que desejas depositar.\n"))
    conta["saldo_atual"] += deposito
    print(f"Depósito de R$ {deposito} realizado com sucesso.\n")

def realizar_saque(conta):
    saque = float(input("Digite, em reais, a quantidade que desejas sacar.\n"))
    if saque <= conta["saldo_atual"]:
        print(f"Saque de R$ {saque} realizado com sucesso.\n")
        conta["saldo_atual"] -= saque
    else:
        print("Você não possui saldo suficiente para realizar tal saque.\n")

def obter_extrato(conta):
    print(f"Nome do usuário : {conta['usuario']['nome']}\n" +
          f"Saldo atual : R$ {conta['saldo_atual']}")

def remover_conta(usuario, contas):
    numero_conta = input("Digite o número da conta que deseja remover: ")
    conta = valida_conta(usuario, contas, numero_conta)

    if conta is not None:
        if conta["saldo_atual"] > 0:
            print(f"Conta {conta['numero_conta']} com saldo igual a R$ {conta['saldo_atual']}.\n")
            resposta = int(input("Não será possível recuperar o dinheiro após remoção da conta. Quer mesmo remover a conta sem sacar antes?\n 0 - Não \n 1 - Sim\n"))

            if resposta == 0:
                print("Sábia decisão.\n")
            elif resposta == 1:
                print("Decisão deveras equivocada e precipitada. Mas como disse Sartre, o humano está condenado a ser livre.\n")
                contas.remove(conta)
            else:
                print("Opção impossível.\n")
    else:
        print("Conta não encontrada.\n")

def main():
    usuarios = []
    contas = []
    iniciar_interacao(usuarios, contas)

if __name__ == "__main__":
    main()
