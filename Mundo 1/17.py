from math import pow,sqrt

x = float(input("Digite o valor do cateto: "))
y = float(input("Digite o valor do cateto oposto:"))

x = pow(x,2)
y = pow(y,2)
soma = x + y
print("A hipotenusa é igual á = {:.2f}".format(sqrt(soma)))


