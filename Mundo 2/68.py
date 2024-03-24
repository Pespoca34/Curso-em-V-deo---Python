from random import randint

pc = randint(1,10)
vp = vpc = soma = 0

while(1):
    player = int(input('Digite um número: '))
    soma = pc + player
    escolha = str(input('Par ou Ímpar[P/I]: ')).upper().strip()
    if(escolha == 'P'):
        if(soma % 2 == 0):
            vp += 1
            soma = 0
        else:
            print(f'Você ganhou {vp} vezes')
            break
    if(escolha == 'I'):
        if(soma % 2 != 0):
            vp += 1
            soma = 0
        else:
            print(f'Você ganhou {vp} vezes')

print('Obrigado por jogar comigo ^-^')