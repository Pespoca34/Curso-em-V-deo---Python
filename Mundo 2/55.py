listap = []
maior = 0 
menor = 0
for i in range(5):
    peso = float(input(f'Digit o peso da {i+1} pessoa: ')) 
    if(i == 0):
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O valor do maior e do menor peso são respectivamente {maior} e {menor}')

#! Consigo fazer comparando lista usando MAX e MIN