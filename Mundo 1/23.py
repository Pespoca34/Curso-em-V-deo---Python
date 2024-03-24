x = int(input("Digite um número: "))

uni = x % 10 
dez = (x // 10) % 10
cen = ((x // 10) // 10) % 10
mil = (((x // 10) // 10) // 10)
print(f"Unidades = {uni}\nDezenas = {dez}\nCentenas = {cen}\nMilhares = {mil}")