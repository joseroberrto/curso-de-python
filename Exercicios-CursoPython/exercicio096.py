def area(a,b):
    atotal = a * b
    print()
    print(f'O espaço de dimensções {a}m x {b}m')
    print(f'Possui área igual a {atotal} m²')


largura = float(input('Digite a largura em M:  '))
comprimento = float(input('Dogite o comprimento em M: '))
area(largura,comprimento)