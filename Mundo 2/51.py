termo = int(input("Digite o 1º termo: "))
razao = int(input("Digite a razão da P.A: "))
decimo = termo + (9) * razao
for i in range(termo,decimo + razao,razao):
    print(termo, end=' ')
    termo += razao