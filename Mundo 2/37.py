num = int(input("Digite um número inteiro: "))
y = int(input(("Escolha uma opção:\n[1] - Converter para \033[2;36mBINÁRIO\033[m\n[2] - Converter  para \033[2;35mOCTAL\033[m\n[3] - Converter para \033[2;33mHEXADECIMAL\033[m\n")))
binary = bin(num)
octal = oct(num)
hexa = hex(num)    

if(y == 1):
    print(binary[2:])
elif(y == 2):
    print(octal[2:])
elif(y == 3):
    print(hexa[2:])