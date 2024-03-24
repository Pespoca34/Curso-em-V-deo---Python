from time import strftime,gmtime

anoatual = int(strftime("%Y",gmtime()))
ano = int(input("Digite o ano de nascimento: "))
idade = anoatual - ano
print(idade)
if(idade <= 9):
    print('Mirim')
elif(idade <= 14):
    print("Infantil")
elif(idade <= 19):
    print("Junior")
elif(idade <= 25):
    print("Senior")
else:
    print("Master")
