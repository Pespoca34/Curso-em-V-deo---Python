
velocidade = int(input("Digite a velocidade do carro:\n"))
#! Se ultrapassar 80km/h ele é multado R$ 7.00 por km acima da cota
multa = (velocidade - 80) * 7
if velocidade > 80:
    print("A multa é de R${}.".format(multa))
else:
    print("Está na velocidade ideal.")