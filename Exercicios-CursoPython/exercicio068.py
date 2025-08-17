from random import randint , choice
while True:
	escolha_jogador= int(input('Escolha um número:  '))
	jogador = str(input('Par ou Impar [P/I] :   ')).strip().upper()[0]
	lista = ['P' , 'I']
	
	computador=  choice(lista)#P ou I
	escolha_pc= randint (1,10)# Numero
	
	contagem = escolha_jogador + escolha_pc

	if jogador in 'Pp':
		if computador in 'P':
			if contagem %2 ==0 :
				print('EMPATOU')
	elif jogador in 'Ii' :
		if computador in 'I':
			if contagem %2 == 0:
				print('EMPATOU')
	elif jogador in 'Pp':
		if computador in 'I' :
			if contagem %2 == 0 :
				print('JOGADOR GANHOU')
			else :
				print('COMPUTADOR GANHOU')
				break
	elif jogador in 'Ii':
		if computador  in 'P':
			if contagem %2 == 0:
				print('COMPUTADOR GANHOU')
				break
			else :
				print('JOGADOR GANHOU')

	print(f'Jogador escolheu {jogador} e pc {computador}')
	print(f'Jogador escolheu {escolha_jogador} e pc {escolha_pc}')