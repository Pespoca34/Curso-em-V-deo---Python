cateto1 =int(input("Digite o valor do segmento: "))
cateto2 =int(input("Digite o valor do segmento: "))
hipotenusa = int(input("Digite o valor do segmento: "))

if(cateto1 == cateto2 and cateto2 == hipotenusa):
    print("Triângulo Equilátero.")
if(cateto1 == cateto2 or cateto2 == hipotenusa or cateto1 == hipotenusa):
    print("Triângulo Isósceles.")
else:
    print("Triângulo Escaleno.")