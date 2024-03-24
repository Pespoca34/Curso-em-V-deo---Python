# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. 0 se quiser ver o ano atual
from time import strftime, gmtime
ano = int(input('Digite o ano desejado: '))
anoatual = int(strftime("%Y", gmtime()))
if ano == 0:
    if (anoatual % 4 == 0 and anoatual % 100 != 0) or (anoatual % 400 == 0):
        print(f'O ano {anoatual} é bissexto!')
    else:
        print(f"O ano {anoatual} não é bissexto!")
else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f'O ano {ano} é bissexto!')
    else:
        print(f"O ano {ano} não é bissexto!")