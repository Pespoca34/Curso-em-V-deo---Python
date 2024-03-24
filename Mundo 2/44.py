preco = int(input("Digite o preço: "))
print("---Digite a opção---\n[1] - A Vista no dinheiro\n[2] - A Vista no Cartão\n[3] - 2x no Cartão\n[4] - 3x ou mais parcelas no Cartão")
opcao = int(input('Opção = '))
if(opcao == 1):
    print("O valor final do produto é igual à R${}".format(preco * 0.9))
elif(opcao == 2):
    print("O valor final do produto é igual à R${}".format(preco * 0.95))
elif(opcao == 3):
    print(f"O valor continuar igual, R${preco}")
else:
    print(f"O valor final é igual à {preco * 1.2}")