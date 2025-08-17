principal= list()
temporario = list()
tot = 0
maior = menor = 0

while True:
	temporario.append(str(input('Nome:  ')))
	temporario.append(float(input('Peso:  ')))
	if len(principal) == 0:
		maior=menor = temporario[1]
	else:
		if temporario[1] > maior:
			maior = temporario[1]
		if temporario[1] < menor:
			menor = temporario[1]
	principal.append(temporario[:])
	tot += 1 
	temporario.clear()	
	resposta = str(input('Quer continuar?[S/N] '))
	print('-=-' * 20)
	if resposta in 'Nn':
		break
	

print(f'Foram cadastradas {tot} pessoas')
print(f'O maior peso foi {maior} kg.De ' , end='')
for p in principal:
	if p[1] == maior:
		print(f'{p[0]}')
print(f'O menor peso foi {menor} kg .De ' , end='')
for p in principal:
	if p[1] == menor:
		print(f'{p[0]}' )
