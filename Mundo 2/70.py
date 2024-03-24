# A- Qual o total gasto
# B- Quantos produtos menor que 1000
# C- Qual o nome do produto mais barato

quantidade = total = menor = menorde100 = 0
barato = ""


print("--------------------------------")
print("       LOJA SUPER BARATÃO")
print("--------------------------------")
while(1):
    nome = str(input("Nome do produto: ")).capitalize().strip()
    preco = int(input("Preço: "))
    quantidade += 1
    if(preco > 1000):
        menorde100 += 1
    if(quantidade == 1):
        menor = preco
        barato = nome
        total += preco
    else:
        total += preco
        if(preco < menor):
            barato = nome
            menor = preco
    continua = str(input("Continuar[S/N]: ")).upper().strip()
    if(continua == 'N'):
        print(f'O total da compra foi R$ {total}')
        print(f'Temos {menorde100} produtos custando mais de 1000')
        print(f'O produto mais barato foi {barato} com o preço de {menor}')
        break