from random import shuffle
v = []
for i in range(4):
    y = str(input("Digite um Aluno: "))
    v.append(y)

shuffle(v)
print("{}".format(v))

