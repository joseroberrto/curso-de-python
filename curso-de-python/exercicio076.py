#variavel tupla
produtos = 'Pao' , 0.6 , 'Café' , 7 , 'Oleo' , 8.90 , 'Arroz' , 5 , 'Suco' , 0.99 , 'Açucar', 3

#Titulo e charme
print('==' *16)
print(f'{'TABELA DE PREÇOS':^50}')
print('==' * 16)

#for para colocar os elementos na vertical
for pos in range(0 , len(produtos)) :
	if pos %2== 0: # itens estao na posicao par
		print(f'{produtos[pos]:.<50}', end='')
	else : # preços estao na posicao impar
		print(f'R${produtos[pos]:>1.2f}')
print('FIM')