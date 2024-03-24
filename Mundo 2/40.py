nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2
if(media >= 7):
    print("Aprovado!")
elif(6.9 >= media >= 5):
    print("Recuperação!")
elif(media < 5):
    print("Reprovado!")