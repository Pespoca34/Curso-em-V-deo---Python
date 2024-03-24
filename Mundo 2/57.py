letra = ''

while (True):
    letra = str(input("Infore o seu sexo: [M/F]: ")).upper().strip()
    if(letra == 'M' or letra == 'F'):
        print(f"Sexo {letra} registrado com sucesso")
        break;
    else:
        continue;
    