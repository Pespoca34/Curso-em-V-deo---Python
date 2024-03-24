from math import tan, sin, cos, radians

x = float(input("Digite o ângulo: "))
y = radians(x)
print("O Valor do seno do Ângulo é igual à = {:.2f}".format(sin(y)))
print("O Valor do cosseno do Ângulo é igual à = {:.2f}".format(cos(y)))
print("O Valor da tangente do Ângulo é igual à = {:.2f}".format(tan(y)))