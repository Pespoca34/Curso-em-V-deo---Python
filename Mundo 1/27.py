nome = str(input("Digite o seu nome:\n")).strip().title().split()
print(f"Muito prazer me te conhecer!\nSeu primeiro nome é = {nome[0]}\nSeu último nome é = {nome[len(nome)-1]}")