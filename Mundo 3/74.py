from random import randint

numeros = (randint(1,10), randint(1,10),randint(1,10),
           randint(1,10), randint(1,10))

for i in range(len(numeros)):
    print(numeros[i],end='->')
print()
print(max(numeros))
print(min(numeros))