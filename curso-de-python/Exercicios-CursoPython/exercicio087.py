matriz = [[0,0,0] , [0,0,0] , [0,0,0]]

for l in range(0,3):
	for c in range(0,3):
		matriz[l][c] = int(input(f'Digite um valor para a posicao {[l , c]}'))

for l in range(0,3):
	for c in range(0,3):
		print(f'[{matriz[l][c]:^5}]' , end=' ')
	print( )

somapar =0
somater = 0
maior = 0
for l in range(0,3):
	for c in range(0,3):
		if matriz[l][c] %2 == 0:
			somapar += matriz[l][c]
		if c == 2:
			somater += matriz[l][c]
		if l == 1 :
			maior = matriz[l][c]
			if matriz[l][c]> maior:
				maior = matriz[l][c]
			
			
print(f'A soma dos valores pares é {somapar}')
print(f'A soma da 3° coluna é {somater}')
print(f'O maior valor da 2° linha é {maior}')