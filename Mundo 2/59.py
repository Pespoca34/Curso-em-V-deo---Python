num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = 0
while opcao != 5:
    print("=================")
    print("""[ 1 ] Multiplicar
[ 2 ] Maior número
[ 3 ] Novos números
[ 4 ] Somar
[ 5 ] Sair do programa""")
    opcao = int(input("Digite a operação que você deseja: "))
    if(opcao == 1):
        print(f"A soma é igual à: {num1 * num2}")
    elif(opcao == 2):
        print("O maior número é igual à {}".format(max(num1,num2)))
    elif(opcao == 3):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif(opcao == 4):
        print(f"A soma dos valores é igual à {num1 + num2}")
print("Fim do programa! Volte sempre!")