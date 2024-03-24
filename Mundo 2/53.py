frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)
invertido = ''

for i in range(len(frase) - 1,-1,-1):
    invertido += frase[i]

if(invertido == frase):
    print('É palíndromo')
else:
    print('Não é palíndromo')