from time import strftime,gmtime

maior = 0
menor = 0
anoatual = int(strftime("%Y",gmtime()))
for i in range(0,7):
    ano = int(input((f'Digite o ano que a {i+1}º nasceu: ')))
    if(anoatual - ano >= 18):
        maior += 1
    elif(anoatual - ano < 18):
        menor += 1
print(f'Tivemos {maior} maiores de idade.\nTivemos {menor} menores de idade')