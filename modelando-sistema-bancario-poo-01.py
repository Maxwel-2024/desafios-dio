import textwrap

def mostrar_menu():
    menu = """
    ========== MENU BANCÁRIO ==========
    [1] Realizar depósito
    [2] Realizar saque
    [3] Consultar extrato
    [4] Criar nova conta
    [5] Listar contas cadastradas
    [6] Cadastrar novo usuário
    [0] Encerrar o programa
    ------------------------------------
    Selecione a opção desejada:
    """
    return input(textwrap.dedent(menu))


def fazer_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: +R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Valor de depósito inválido. Tente novamente.")
    return saldo, extrato

def fazer_saque(*, saldo, valor, extrato, limite, saques_realizados, max_saques):
    sem_fundos = valor > saldo
    acima_limite = valor > limite
    atingiu_saques = saques_realizados >= max_saques

    if sem_fundos:
        print("Saldo insuficiente para saque.")

    elif acima_limite:
        print("Valor solicitado excede o limite permitido para saque.")

    elif atingiu_saques:
        print("Limite diário de saques atingido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:   -R$ {valor:.2f}\n"
        saques_realizados += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor inválido para saque.")

    return saldo, extrato, saques_realizados

def mostrar_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Nenhuma movimentação registrada.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================")

def cadastrar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")
    if buscar_usuario(cpf, usuarios):
        print("Usuário já cadastrado para este CPF.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, número, bairro, cidade/UF): ")

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def buscar_usuario(cpf, usuarios):
    filtrados = [u for u in usuarios if u["cpf"] == cpf]
    return filtrados[0] if filtrados else None

def criar_nova_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do titular: ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}
    else:
        print("CPF não encontrado. Conta não criada.")

def exibir_contas(contas):
    for conta in contas:
        info = f"""
        Agência:        {conta['agencia']}
        Conta número:   {conta['numero_conta']}
        Titular:        {conta['usuario']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(info))

def main():
    MAX_SAQUES = 3
    CODIGO_AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            valor = float(input("Valor para depósito: "))
            saldo, extrato = fazer_deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Valor para saque: "))
            saldo, extrato, saques_realizados = fazer_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques_realizados=saques_realizados,
                max_saques=MAX_SAQUES,
            )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            num_conta = len(contas) + 1
            conta = criar_nova_conta(CODIGO_AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            exibir_contas(contas)

        elif opcao == "6":
            cadastrar_usuario(usuarios)

        elif opcao == "0":
            print("Saindo... Obrigado por utilizar nosso sistema bancário!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()