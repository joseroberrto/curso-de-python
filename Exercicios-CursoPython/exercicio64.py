numeros = 0 
totdigitos = 0
totalsoma = 0

#repeticao ate o usuario digitar condicao de parada
while numeros != 999:
	numeros = int(input('Digite um numero : '))
	print('Digite 999 quando quiser parar')
	if numeros != 999: #condicao para colocar o charme
		print('--' * 30)
		totdigitos = totdigitos + 1#contador 
		totalsoma  = totalsoma + numeros#somador

#final e charme pro programa
print('-×' * 25)
print(f'\033[32mVoce digitou {totdigitos } números')
print(f'E a soma entre os números digitados foi {totalsoma } \033[m')
print('-×' * 25)