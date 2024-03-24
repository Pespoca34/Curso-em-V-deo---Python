"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

distancia = int(input("Digite a quantidade em Kilometros:\n"))

if distancia <= 200:
    print(f"O valor é {distancia * 0.5}")
else:
    print(f"O valor é {distancia * 0.45}")