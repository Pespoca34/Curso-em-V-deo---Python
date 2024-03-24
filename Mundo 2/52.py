num = int(input("Digite um número: "))
cont = 0
lista = []
for i in range(1,num+1):
    if (num % i == 0):
        cont += 1
        lista.append(i)
if cont > 2:
    print(f'O número foi divisível {cont} vezes pelos números {lista}, logo não pode ser primo')
else:
    print(f'É primo papai')
