#SISTEMA BANCÁRIO SIMPLES. 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

menu = """MENU
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR
>>"""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("-- DEPÓSITO --")
        deposito = float(input("Qual valor do seu depósito? R$: "))
        if deposito <= 0:
            print("Valor inválido, digite um valor válido.")
        else:
            print(f"Depósito de R${deposito:.3f} foi realizado com sucesso.")
            saldo += deposito
            extrato += f"DEPÓSITO: +R${deposito:.3f}\n"

    elif opcao == 2:
        print("-- SAQUE --")
        saque = float(input("Qual valor do seu saque? R$: "))
        if saque <= 0:
            print("Valor inválido, digite um valor válido.")
        elif saque > limite:
            print("Valor do saque excede o limite permitido.")
        elif numero_saques >= LIMITE_SAQUE:
            print("Limite de saques diários excedido.")
        elif saque > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print(f"Saque de R${saque:.3f} foi realizado com sucesso.")
            saldo -= saque
            extrato += f"SAQUE: -R${saque:.3f}\n"
            numero_saques += 1

    elif opcao == 3:
        print("-- EXTRATO --")
        print("Transações:")
        print(extrato)
        print(f"Saldo atual: R${saldo:.3f}")

    elif opcao == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida, selecione uma opção válida.")

