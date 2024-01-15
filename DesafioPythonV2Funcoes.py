import textwrap as tw


def menu():
    menu = """\n
    -------------------------MENU-------------------------
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Cadastrar cliente
    [5]Criar contas
    [6]Listar contas
    [0]Sair
    ------------------------------------------------------\n
    DIGITE A OPÇÃO DESEJADA:
    """
    return input(tw.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f"\nDepósito no valor de R${valor:.2f} realizado com sucesso!!!")
    else:
        print("\nDEPOSITO FALHOU! Favor repetir o processo.")
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, qnt_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = qnt_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insfuciente")
    elif excedeu_limite:
        print("Valor de saque maior que o permitido")
    elif excedeu_saques:
        print("Excedeu numero de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R$:{valor:.2f}\n"
        print("-------Saque realizado com sucesso!!!-------")
    else:
        print("informe um valor valido")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("========EXTRATO========")
    print("sem movimentações" if not extrato else extrato)
    print(f"Saldo atual R$:{saldo:.2f}")
    print("========FIM========")

def cadastrar_usuario(usuarios):
    cpf = input("Informe o cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado.")
        return
    
    nome = input("Digite o nome do cliente: ")
    data_nasc = input("Data nascimento(dd-mm-aaaa): ")
    endereco = input("Endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco})

    print("cadastro ook")
    
def filtrar_usuario(cpf, usuarios):
    user_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return user_filtrados[0] if user_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!!!. ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado! Favor cadastrar o cliente.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            Conta: \t\t{conta['numero_conta']}
            Titutal: \t{conta['usuario']['nome']}
        """
        print("="*100)
        print(tw.dedent(linha))