conta_normal = False
conta_universitaria = True

saldo = 5000
saque = 2500
cheque_especial = 500
saldo_conta_especial = saldo + cheque_especial

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
        saldo -= saque
        print("Saldo atual:", saldo)
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
        saldo_conta_especial -= saque
        print("Saldo atual:", saldo_conta_especial)
    else:
        print("Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
        saldo -= saque
        print("Saldo atual:", saldo)
    else:
        print("Saldo insuficiente!")
else:
    print("Não há conta!")
