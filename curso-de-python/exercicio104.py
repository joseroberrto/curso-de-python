def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRORR')
        if ok :
            break
    return valor

n = leia_int('Digite um número')
print(f'Você digitou {n}')