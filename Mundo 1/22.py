"""Crie um programa que leia o nome completo de uma pessoa e mostre: 
- Quantas letras tem o primeiro nome."""

nome = str(input("Digite seu nome completo:\n")).strip()
print(f'UPPER = {nome.upper()}')
print(f'LOWER = {nome.lower()}')
lista = nome.split()
nome1 = lista[0]
lista = ''.join(lista)
print(f"{len(lista)}")
print(f"O primeiro nome é = {nome1.capitalize()}")
print(f"O primeiro nome tem = {len(nome1)}")