a1 = 0
a2 = 1
fibo = int(input("Digite a quantidade de números: "))
for i in range(0, fibo):
    n = a1 + a2
    print(f"{a1}", end='-')
    a1 = a2
    a2 = n
    