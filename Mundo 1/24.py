nome = str(input("Digite o seu nome: ")).strip().lower()
nome = nome.split()
verificador = nome[0]

if verificador == 'santo':
    print(True)
else:
    print(False)