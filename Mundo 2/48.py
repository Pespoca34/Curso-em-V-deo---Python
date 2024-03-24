soma = 0
cont = 0
for i in range(0,501):
    if(i % 2 != 0):
        if(i % 3 == 0):
            soma += i
            cont += 1
print(soma,cont)