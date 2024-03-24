print("----Calcular Fatorial----")
num = int(input("Digite um número: "))
fatorial = 1
aux = num

while (aux > 0):
    fatorial = fatorial * aux
    aux -= 1


print(f"Fatorial é igual à {fatorial}")