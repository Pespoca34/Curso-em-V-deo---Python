from random import choice
v = []
for i in range(4):
    y = str(input("Digite um nome: "))
    v.append(y)

print("O aluno escolhido é = {}".format(choice(v)))