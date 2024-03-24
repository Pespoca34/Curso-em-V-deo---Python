numeros = ("um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "catorze", "quinze",
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")



x = int(input("Digite um número de 0 à 20: "))
if(x == 0):
    print('0')
else:
    print(numeros[x-1])