from random import randint
numeros = list()


def sorteio(lst):
    for c in range(0,5):
        lst.append(randint(0,10))
    print('Os números sorteados foram:',end='')
    print(lst)


def somapares(lst):
    totsoma = 0
    for n in lst:
        if n %2 == 0:
            totsoma += n
    print(f'A soma dos números pares é {totsoma}')


sorteio(numeros)
somapares(numeros)