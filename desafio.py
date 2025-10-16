menu1 = """
[n] Novo usuário
[c] Nova conta corrente
[a] Abrir menu banco
[q] Sair
=> """
menu2 = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
contacorrente = 0
def depositar(valor):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
            return print("Operação falhou! O valor informado é inválido.")
def sacar(valor):
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
def extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def newUser():
    cpf = input("Informe o CPF (somente números): ")
    if(cpf in usuarios):
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    if(endereco == "" or data_nascimento == "" or nome == ""):
        print("Erro no cadastro do usuário, verifique os dados.")
        return
    print(f"Usuário {nome} cadastrado com sucesso!")
def criarConta():
    contas = dict(
        agencia="0001",
        numero=contacorrente,
        usuario=usuarios
    )
    contacorrente += 1
    return contas
while True:

    opcao = input(menu1)
    
    if(opcao == "a"):
        opcao = input(menu2)
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
       
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        
        elif opcao == "e":
            extrato()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    elif(opcao == "n"):
        usuarios = newUser()
    elif(opcao == "c"):
        criarConta()
    elif(opcao == "q"):
        break
    else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")