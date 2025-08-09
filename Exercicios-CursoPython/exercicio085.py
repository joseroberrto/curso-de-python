listnum = [ [ ] , [ ] ]


for c in  range(1,8):
	val = int(input(f'Digite um valor p/ posicao {c}:'))
	if val%2 ==0 :
		listnum[0].append(val)
	else :
		listnum[1].append(val)

print('-=-' * 20)	
listnum[0].sort()
listnum[1].sort()

print(f'A lista de numeros pares: {listnum[0]}')
print(f'A lista de numeros impares:{listnum[1]}')
	