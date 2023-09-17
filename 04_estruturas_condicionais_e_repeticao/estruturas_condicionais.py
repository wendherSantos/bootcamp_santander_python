MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade! Poderá retirar a CNH.")
if idade < MAIOR_IDADE:
    print("Você é menor de idade! Não poderá retirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade! Poderá retirar a CNH.")
else:
    print("Você é menor de idade! Não poderá retirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade! Poderá retirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Você tem 17 anos e pode fazer as aulas teóricas.")
else:
    print("Você é menor de idade! Não poderá retirar a CNH.")
