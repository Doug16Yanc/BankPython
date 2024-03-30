from abc import ABC, abstractclassmethod
import sys

class Transacao(ABC):
    def registrar_conta(transacao):
        return list

class Cliente():
    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = contas

        @property
        def endereco(self):
            self._endereco = endereco

        @property
        def contas(self):
            self._contas = contas

class Pessoa_Fisica(Cliente):
    def __init__(self, endereco, contas, cpf, nome, data_nascimento, senha):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._senha = senha

        @property
        def cpf(self):
            self._cpf = cpf

        @property
        def nome(self):
            self._nome = nome 
        
        @property
        def data_nascimento(self):
            self._data_nascimento = data_nascimento

        @property
        def senha(self):
            self._senha = senha

class Conta():
    def __init__(self, cliente, saldo, numero, agencia, historico): 
        self._cliente = cliente
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._historico = historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero) 
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    
    @property
    def historico(self):
        return self._historico
    



class Conta_Corrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques
        
        @property 
        def limite(self):
            self._limite = limite
        
        @property
        def limite_saques(self):
            self._limite_saques = limite_saques

class Deposito():
    def __init__(self, valor):
        self._valor = valor

        @property
        def valor(self):
            self._valor = valor

class Saque():
    def __init__(self, valor):
        self._valor = valor

        @property
        def valor(self):
            self._valor = valor




def iniciar_interacao(usuarios, contas):
    while True :
        print("Olá, caríssimo usuário.\n")
        resposta = input("já é cadastrado em nossa plataforma?\n S/s - Sim \n N/n - Não\n O/o - Sair\n")

        if resposta.lower() == 'n':
            cadastra_usuario(usuarios, contas)
        elif resposta.lower() == 's':
            faz_login(usuarios, contas)
        elif resposta.lower() == 'o':
            sys.exit()
        else:
            print("Opção impossível.\n")
            sys.exit()

def cadastra_usuario(usuarios, contas):
    nome = input("Nome : ")
    cpf = input("Cadastro de pessoa física : ")
    endereco = input("Digite o endereço : ")
    data_nascimento = input("Data de nascimento : ")
    senha = input("Senha para acesso ao sistema : ")


    usuario = Pessoa_Fisica(endereco, contas, cpf, nome, data_nascimento, senha)

    usuarios.append(usuario)


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
        if usuario._cpf == cpf and usuario._senha == senha:
            return usuario
    return None

def visualizar_dados(usuario):
    print("Dados do usuário: \n")
    print(f"Nome: {usuario._nome}\n" +
    f"CPF: {usuario._cpf}\n" +
    f"Endereço: {usuario._endereco}")

def interage_usuario(usuario, contas):
    saiu = False
    while True:
        print(f"Bem-vindo(a) ao seu menu de opções deste extraordinário sistema bancário, caríssimo(a) {usuario._nome}.\n")
        opcao = int(input("Escolha uma opção para realizar:\n" +
                        "0 - Sair\n" +
                        "1 - Criar conta\n" +
                        "2 - Ir para a conta\n" +
                        "3 - Visualizar dados\n" +
                        "4 - Remover conta\n"))

        if opcao == 0:
            print(f"Sua despedida é sempre tão dolorosa, caro {usuario._nome}. Espero te ver logo.\n")
            saiu = True
            break
        elif opcao == 1:
            criar_conta(usuario, contas)
        elif opcao == 2:
            oferta_opcoes_conta(usuario, contas)
        elif opcao == 3:
            visualizar_dados(usuario)
        elif opcao == 4:
            remover_conta(usuario, contas)
        else:
            print("Opção impossível. Por favor, escolha uma que seja possível.\n")

    if saiu :
        return


def criar_conta(usuario, contas):
    saldo = 0.0
    numero = input("Número : ")
    agencia = input("Agência : ")
    historico = 0
    limite = 200000
    limite_saques = 3

    conta = Conta_Corrente(usuario, saldo, numero, agencia, historico, limite, limite_saques)

    contas.append(conta)

def oferta_opcoes_conta(usuarios, contas):
    numero_conta = input("Digite o número da conta:")

    conta_validada = valida_conta(contas, numero_conta)

    if conta_validada is not None:
        print("Selecione uma opção.\n")
        opcao = int(input("\n1 - Realizar depósito : " +
                        "\n2 - Realizar saque : " +
                        "\n3 - Obter extrato : \n"))
                            
        if opcao == 1:
            realizar_deposito(conta_validada)
        elif opcao == 2:
            realizar_saque(conta_validada)
        elif opcao == 3:
            obter_extrato(conta_validada)
        else:
            print("Opção impossível.\n")
    else :
        print("Conta não encontrada.")

def valida_conta(contas, numero_conta):
    for conta in contas:
        if conta._numero == numero_conta:
            
            return conta
    print("Conta não encontrada.\n")
    return None

def realizar_deposito(conta):
    deposito = float(input("Digite, em reais, a quantidade que desejas depositar.\n"))
    conta._saldo += deposito
    transacao = Deposito(deposito)
    registrar_conta(transacao)
    print(f"Depósito de R$ {deposito} realizado com sucesso.\n")

def realizar_saque(conta):
    saque = float(input("Digite, em reais, a quantidade que desejas sacar.\n"))
    if conta._limite_saques <= 3 :
        if saque <= conta._saldo:
            print(f"Saque de R$ {saque} realizado com sucesso.\n")
            conta._saldo -= saque
            conta._limite_saques += 1
            transacao = Saque(saque)
            registrar_conta(transacao)

        else:
            print("Você não possui saldo suficiente para realizar tal saque.\n")
    else:
        print("Você já excedeu o limite de saques hoje.")

def obter_extrato(conta):
    print(f"Nome do usuário : {conta._cliente._nome}\n" +
        f"Saldo atual : R$ {conta._saldo}")

def remover_conta(usuarios, contas):
    numero_conta = input("Digite o número da conta que deseja remover: ")
    conta = valida_conta(contas, numero_conta)

    if conta is not None:
        if conta._saldo > 0:
            print(f"Conta {contas._numero} com saldo igual a R$ {conta._saldo}.\n")
            resposta = int(input("Não será possível recuperar o dinheiro após remoção da conta. Quer mesmo remover a conta sem sacar antes?\n 0 - Não \n 1 - Sim\n"))

            if resposta == 0:
                print("Sábia decisão.\n")
            elif resposta == 1:
                print("Decisão deveras equivocada e precipitada. Mas como disse Sartre, o humano está condenado a ser livre.\n")
                contas.remove(conta)
            else:
                print("Opção impossível.\n")
        else:
            contas.remove(conta)
    else:
        print("Conta não encontrada.\n")


def registrar_conta(transacao):
    transacoes = [] 
    transacoes.append(transacao)


def main():
    usuarios = []
    contas = []
    print("Bem-vindo ao nosso sistema bancário.\n")
    iniciar_interacao(usuarios, contas)


if __name__ == '__main__':
    main()