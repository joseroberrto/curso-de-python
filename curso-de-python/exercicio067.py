
while True : # loop 
	numero = int(input('Qual número quer a tabuada?  '))
	print('-=-' * 20)
	if numero < 0: #condicao de parada
		break
	for t in range(1,11): #repeticao para formar a tabuada 
		print(f'{numero} × { t :2} = {numero*t :3}')
	print('-=-' * 20)	
	
#fim do programa
print('Tabuada Encerrada , volte sempre !')
	