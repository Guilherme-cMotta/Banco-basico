def extrato (saldo):
    print(f"\nSeu saldo atual é: R${saldo:.2F}")

def saque (saldo):
    valor = float(input("\nDigite o valor do saque: "))
    if valor > saldo:
        print("Operação invalida, saldo insuficiente")
    else:
        saldo -= valor
        print("\nSaque realizado com sucesso!")
    return saldo

def deposito (saldo):
    valor = float(input("Digite o valor do depósito: "))
    saldo += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    return saldo

saldo = 0.0

while True:
    print("\nMenu\n")   
    print("1. Extrato")
    print("2. Saque")
    print("3. Depósito")
    print("4. Sair\n")

    option = int(input("Selecione a opção desejada: "))

    if option == 1:
        extrato(saldo)
    elif option == 2:
        saldo = saque(saldo)
    elif option == 3:
        saldo = deposito(saldo)
    elif option == 4:
        print("Finalizando!\n")
        break
    else:
        print("Opção invalida!")