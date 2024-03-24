numeros = ('Um', 'Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze',
           'Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    escolha = int(input("Digite um número de 0 à 20: "))
    if(escolha == 0):
        print("Zero")
    elif(escolha > 20 or escolha < 0):
        print('Número inválido!')
        pass
    else:
        print(numeros[escolha-1])
    continuar = str(input("Quer continuar?[S/N]: ")).upper().strip()
    if(continuar == 'S'):
        continue
    else:
        break;
print('Obrigado ^-^')