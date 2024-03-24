soma = cont = 0

while(1):
    x = int(input("Digite um número(999- Parar): "))
    if(x == 999):
        print(f'A soma dos {cont} é igual à {soma}')
        break
    else:
        soma += x
        cont += 1

