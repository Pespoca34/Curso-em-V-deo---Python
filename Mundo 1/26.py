"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

frase = str(input("Digite sua frase:\n")).strip().lower()
x = frase.count('a')
posicao = frase.find('a')
posicaoultima = frase.rfind('a')
print(f"Quantidade de vezes = {x}\nPrimeira posição = {posicao + 1}\n Ultima posição = {posicaoultima + 1}")