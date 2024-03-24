num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

if(num1 > num2):
    print(f'{num1} é maior.')
elif(num1 < num2):
    print(f"{num2} é maior.")
elif(num1 == num2):
    print('Os dois são iguais.')