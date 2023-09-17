texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# iteravel
for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end="")


# built-in range
for numero in range(0, 51, 5):
    print(numero)
