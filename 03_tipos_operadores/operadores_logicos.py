# AND = tudo tem que ser True
# OR = apenas um True

print(True and True)
print(True and False)
print(True or False)
print(True or True)
print(False or False)
print(False and False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

