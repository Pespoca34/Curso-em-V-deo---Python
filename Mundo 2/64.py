quantidade = 0
soma = 0
n = 0
while (n != 999):
    n = int(input("Digite um número(999 stop): "))
    if(n == 999):
        break;
    else:
        soma += n
        quantidade += 1

print(f'{quantidade} números digitados e a soma é igual à = {soma}')