def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso!")
        saldo -= valor
        print("Saldo atual:", saldo)

    print("Obrigado por usar nossos serviços!")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(100)

