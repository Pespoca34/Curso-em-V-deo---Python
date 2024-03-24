print("==== CALCULAR A PA ====")

a1 = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = a1
posicao = 1
total = 0
num = 10

while num != 0:
    total = total + num
    while posicao <= total:
        print('{}'.format(termo), end='->')
        termo += razao
        posicao += 1
    print('Pausa')
    num = int(input("Quantos números mais(0 para terminar): "))