nome = str(input("Digite seu nome :")).upper().strip()


print(f'A letra A aparece {nome.count('A')} na frase' )#quantas vezes A apareceu
print(f'A letra A aparece primero na posicao {nome.find('A') + 1}')# indice onde A começou
print(f'A letra A aparece por ultimo na posicao {nome.rfind('A') + 1}')# indice onde A começou pela direita (right)