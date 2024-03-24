respostas = ''
quantidade = menor = maior = 0 
while(respostas != 'N'):
    num = int(input("Digite um número: "))
    quantidade += 1
    
    if(quantidade == 1):
        maior = menor = num
    else:
        if(num > maior):
            maior = num
        elif(num < menor):
            menor = num
    respostas = str(input("Quer continuar? [S/N]: ")).upper().strip()

print(maior, menor, quantidade)