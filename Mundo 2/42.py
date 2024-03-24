"""Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados."""
a = int(input("Digite o valor do 1º segmento: "))
b = int(input("Digite o valor do 2º segmento: "))
c = int(input("Digite o valor do 3º segmento: "))

if(a > abs(b-c) and a < b + c):
    if(a == b and b == c):
        print("Pode ser triângulo, EQUILÁTERO.")
    elif(a == b or b == c or a == c):
        print("Pode ser triângulo, ISÓSCELES.")
    else:
        print("Pode ser triângulo, ESCALENO.")
elif(b > abs(a-c) and b < a + c):
    if(a == b and b == c):
        print("Pode ser triângulo, EQUILÁTERO.")
    elif(a == b or b == c or a == c):
        print("Pode ser triângulo, ISÓSCELES.")
    else:
        print("Pode ser triângulo, ESCALENO.")
elif(c > abs(b-a) and c < a + b):
    if(a == b and b == c):
        print("Pode ser triângulo, EQUILÁTERO.")
    elif(a == b or b == c or a == c):
        print("Pode ser triângulo, ISÓSCELES.")
    else:
        print("Pode ser triângulo, ESCALENO.")
else:
    print("Não pode se formar um triângulo.")