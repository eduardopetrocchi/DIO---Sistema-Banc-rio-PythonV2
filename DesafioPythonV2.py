import DesafioPythonV2Funcoes as func

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    qnt_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = func.menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = func.depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = func.sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                qnt_saques=qnt_saques,
                limite_saques=LIMITE_SAQUES
            )
        
        elif opcao == "3":
            func.exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            func.cadastrar_usuario(usuarios)
        
        elif opcao == "5":
            conta = func.criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif opcao == "6":
            func.listar_contas(contas)
        
        elif opcao == "0":
            print("Obrigado pela atenção!!")
            break

        else:
            print("Insira uma opção válida.")

main()