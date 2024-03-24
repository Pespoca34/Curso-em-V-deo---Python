from math import pow
peso = int(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura: "))
altura = pow(altura,2)
imc = peso / altura
"""- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""
print("IMC = {:.2f}".format(imc))
if(imc < 18.5):
    print("Abaixo do Peso")
elif(imc < 25):
    print("Peso Ideal")
elif(imc < 30):
    print("Sobrepreso")
elif(imc < 40):
    print("Obesidade")
else:
    print("Obesidade Mórbida")