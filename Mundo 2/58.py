from random import randint

print("Pensei num número de 1 à 10, tente adivinhar")
pc = randint(0,10)
contador = 0
while True:
    numero = int(input("Qual o seu palpite ?: "))
    if(numero == pc):
        contador += 1
        print(f"Você acertou em {contador} tentativas")
        break;
    elif (numero > pc):
        contador += 1
        print("Você errou, tente um número menor")
    else:
        contador += 1
        print("Você errou, tente um número maior")