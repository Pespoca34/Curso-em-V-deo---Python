dias = int(input("Quantos dias alugados: "))
km = int(input("Quantos KM rodado: "))
##! 60 reais por dia, 0.15km
valordias = dias * 60
valorkm = km * 0.15
valortotal = valordias + valorkm

print("O total a pagar = {:.2f}".format(valortotal))