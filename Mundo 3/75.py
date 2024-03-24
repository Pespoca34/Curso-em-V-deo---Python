lista = []
for i in range(4):
    num = int(input("Digite um número: "))
    lista.append(num)
tupla = tuple(lista)
print(tupla)
print(tupla.count())