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
saldo = 0.0
limite = 500.0
extrato_text = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
contador_conta = 1
def depositar(valor):
    global saldo, extrato_text
    if valor > 0:
        saldo += valor
        extrato_text += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
def sacar(valor):
    global saldo, extrato_text, numero_saques
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
        extrato_text += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
def extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_text else extrato_text)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def newUser():
    cpf = input("Informe o CPF (somente números): ").strip()
    if any(u["cpf"] == cpf for u in usuarios):
        print("Já existe usuário com esse CPF!")
        return None
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    if not (cpf and nome and data_nascimento and endereco):
        print("Erro no cadastro do usuário, verifique os dados.")
        return None
    usuario = {
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuario
def criarConta():
    global contador_conta
    if not usuarios:
        print("Não há usuários cadastrados. Crie um usuário antes de criar uma conta.")
        return None
    cpf = input("Informe o CPF do titular da conta: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario is None:
        print("Usuário não encontrado. Verifique o CPF.")
        return None
    conta = {
        "agencia": "0001",
        "numero": f"{contador_conta:04d}",
        "usuario": usuario
    }
    contas.append(conta)
    contador_conta += 1
    print(f"Conta criada com sucesso! Agência: {conta['agencia']} Nº: {conta['numero']} Titular: {usuario['nome']}")
    return conta
while True:
    opcao = input(menu1).strip().lower()
    if opcao == "a":
        while True:
            opcao_banco = input(menu2).strip().lower()
            if opcao_banco == "d":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                except ValueError:
                    print("Valor inválido.")
                    continue
                depositar(valor)
            elif opcao_banco == "s":
                try:
                    valor = float(input("Informe o valor do saque: "))
                except ValueError:
                    print("Valor inválido.")
                    continue
                sacar(valor)
            elif opcao_banco == "e":
                extrato()
            elif opcao_banco == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
    elif opcao == "n":
        usuario = newUser()
        if usuario:
            usuarios.append(usuario)
    elif opcao == "c":
        criarConta()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")