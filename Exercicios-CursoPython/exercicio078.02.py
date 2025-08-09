listanum= []

for cont in range(0,5):
	listanum.append(int(input(f'Digite um valor para a posição {cont}°:  ')))

maior = max(listanum)
menor = min(listanum)

print(listanum)
print(f'O maior valor digitado foi {maior} na posicao ',end='')

for i , v in enumerate(listanum):
	if v == maior:
		print(f'{i}..' , end='')

print(f'\nO menor valor digitadk foi {menor} na posiciao ', end='')

for i , v in enumerate(listanum):
	if v == menor:
		print(f'{i}..', end='')