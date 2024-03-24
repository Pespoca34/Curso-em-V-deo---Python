print("----GERADOR DE PA----")

a1 = int(input("Primeiro Termo da PA: "))
razao = int(input("A razão da PA: "))
posicao = 2
termo = a1
#10º termo
while (posicao != 12): #* Pois começou no 2 logo adiciona mais 10
    print(termo, end="->")
    termo = a1 + (posicao - 1) * razao
    posicao += 1
