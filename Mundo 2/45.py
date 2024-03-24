from random import randint
pc = randint(0,2)
print("---Escolha à opção---\n[0] - Pedra\n[1] - Papel\n[2] - Tesoura")
player = int(input("Escolha uma opção: "))
print(f"Jogador = {player}, PC = {pc}")
if(player == 0):
    if(pc == 1):
        print("Você perdeu")
    elif(pc == 0):
        print("Vocês empataram")
    else:
        print("Você ganhou")
elif(player == 1):
    if(pc == 2):
        print("Você perdeu")
    elif(pc == 1):
        print("Vocês empataram")
    else:
        print("Você ganhou")
else:
    if(pc == 0):
        print("Você perdeu")
    elif(pc == 2):
        print("Vocês empataram")
    else:
        print("Você ganhou")