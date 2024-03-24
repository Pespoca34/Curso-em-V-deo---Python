# Verificador se tem SIlVA no nome
nome = str(input("Digite o seu nome:\n")).strip().lower()
nome = nome.title()
print('Silva' in nome)