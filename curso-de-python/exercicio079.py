listanum= []

#loop para add n números 
while True:
	num = int(input('Digite um número:  '))

	if num not in listanum:#para nao haver num  duplicados na lista
		listanum.append(num)
		print('\033[32mNúmero adicionado com sucesso\033[m')
	else: #se num já estiver na lista
		print('\033[31mNúmero duplicado ,nao adicionado\033[m')
	escolha = str(input('Quer continuar?[S/N]  ')).strip()
	
	while escolha not in 'SimsimNaonao':#verifica se é S ou N
		escolha = str(input('Digite novamente.Quer continuar?[S/N]')).strip()
		
	print('-=-'*20)
	if escolha in 'Nn' :#condiçao de parada do loop
		break
print(listanum)