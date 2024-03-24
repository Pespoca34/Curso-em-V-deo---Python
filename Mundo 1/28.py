from random import randint
pc = randint(0,5)
usuario = int(input("Digite o número que você acha: "))
if usuario == pc:
    print("Você acertou!")
else:
    print("Você errou!")