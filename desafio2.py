import textwrap
from abc import ABC, abstractmethod


        
class Conta:
    saldo = 0.0
    numero = 0
    agencia = "0001"
    def saldo(self):
        return self.saldo
    def nova_conta(self, cliente,):
        Conta.numero += 1
        return self.numero
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque: R$ {valor:.2f}")
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor de depósito inválido.")    
class Transacao(ABC, Conta):
    @abstractmethod
    def registrar(self ):
        pass
    def registrar(self, tipo, valor):
        if tipo == "sacar":
            self.sacar(valor)
        elif tipo == "depositar":
            self.depositar(valor)       
class ContaCorrente(Conta):
    limite_saques = 3
    limite = 500.0
class PessoaFisica:
    nome = ""
    cpf = ""
    data_nascimento = ""
class Cliente (Transacao, Conta, PessoaFisica):
    endereço = ""
    contas = []
    def fazerTransação(self, tipo, valor):
        if tipo == "sacar":
            self.sacar(valor)
        elif tipo == "depositar":
            self.depositar(valor)
    def adicionar_conta(self, conta):
        self.contas.append(conta)
class Historico(Transacao):
    transacoes = []
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))




def main():
    conta = Conta()
    cliente = Cliente()
    historico = Historico()

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            conta.sacar(valor)

        elif opcao == "e":
            conta.extrato()

        elif opcao == "nu":
            cliente.adicionar_conta(conta)

        elif opcao == "nc":
            conta.nova_conta(cliente)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
