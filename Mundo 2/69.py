
homems = anos = m20 = 0
while True:
    print('---------------------')
    print('CADASTRE UMA PESSOA')
    print('---------------------')
    idade = int(input("Idade: "))
    sexo = str(input('[M/F]: ')).strip().upper()
    if(sexo == 'M'):
        homems += 1
    if(idade > 18):
        anos += 1
    if(sexo == 'F' and idade < 20):
        m20 += 1
    print('---------------------')
    continua = str(input('Continua[S/N]: ')).upper().strip()
    if(continua == 'N'):
        print(f'Quantidade de pessoas com mais de 18 anos: {anos}')
        print(f'Ao todo temos {homems} homens cadastrados')
        print(f'E temos {m20} mulheres com menos de 20 anos')
        break