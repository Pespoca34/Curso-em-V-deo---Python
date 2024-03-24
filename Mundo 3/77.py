tupla = ('preto', 'macaco','favelado','arrombado','familia')

for palavras in tupla:
    print(f"Na palavra {palavras}",end=' ')
    for letra in palavras:
        if letra in 'aeiou':
            print(letra,end=' ')
    print()