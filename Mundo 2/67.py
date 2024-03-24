while(1):
    x = int(input('Digite um número: '))
    if(x < 0):
        break
    else:
        for i in range(1,11):
            print(f'{x} x {i} = {x * i}')
