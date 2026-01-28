menu = """
==========================
Bem-vindo ao Banco Lorax
==========================

Selecione uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
==========================

"""
saldo = 0
LIMITE = 500
LIMITESAQUES = 3
extrato = ""
numero_saques = 0

while True:
    opcao = input(menu)

#Depósito
    if opcao == "1":
        print("Depósito")
        valor = float(input(("Informe o valor do depósito: ")))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
#Saque
    elif opcao == "2":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE
        excedeu_saques = numero_saques >= LIMITESAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso!\n Você ainda tem {LIMITESAQUES - numero_saques} saques disponíveis hoje.")
        else:
            print("Operação falhou! O valor informado é inválido.")
#Extrato
    elif opcao == "3":
        print("Extrato")
        print("==========================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================")
#Sair
    elif opcao == "0":
        print("Obrigado por usar o Banco Lorax. Até logo!")
        break
