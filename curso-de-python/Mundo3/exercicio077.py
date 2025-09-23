palavras = ( 'caiu ' , 'pedra' , 'amor' , 'salva' , 'arara')


for elemento in palavras :#repete cada elemento da tupla
	print(f'\nNa palavra {elemento.capitalize()} temos ' , end=' ')
	for letra in elemento :#repete cada letra de cada elemento da tupla
		if letra.lower() in 'aeiou':
			print(f'{letra}' , end=' ')