#? Primeiro jeito de fazer
v = []
for item in range(3):
    num = int(input("Digite um número: "))
    v.append(num)
print("O maior número é = {}".format(max(v)))

#* Segundo Jeito de fazer
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if(num1 > num2) and (num1 > num3):
    print(f"{num1}")
elif(num2 > num1) and (num2 > num3):
    print(f"{num2}")
else:
    print(f"{num3}")