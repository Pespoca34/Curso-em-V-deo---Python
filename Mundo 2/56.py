mm20 = 0
idadetotal = 0
maioridade = 0
nomemaior = ''
for i in range(4):
    print(f'--- {i+1}º PESSOA ---')
    nome = str(input('Digite o seu nome: '))
    idade = int(input("Digite a sua idade: "))
    sexo = str(input('[M/F]: ')).upper().strip()
    idadetotal += idade
    if(idade < 20 and sexo == 'F'):
        mm20 += 1
    if(sexo == 'M'):
        if(idade > maioridade):
            maioridade = idade
            nomemaior = nome
print('A idade média é igual à {:.2f}'.format(idadetotal / 4))
print('O homem mais velhor chama-se {} e tem {} anos.'.format(nomemaior.capitalize(), maioridade))
print(f'A quantidade de mulheres abaixo de 20 anos = {mm20}')