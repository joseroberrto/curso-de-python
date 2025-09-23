from random import randint
from time import sleep

opcoes = ('Papel' , 'Tesoura' , 'Pedra')
print(' [0] Papel \n [1] Tesoura \n [2] Pedra')
jogador = int(input('Escolha sua jogada :'))
computador = randint(0 , 2)

print(' \033[33mJO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO \033[m')
print('-+' * 30)
print(f'O jogador escolheu {opcoes[jogador]}')
print(f'computador escolheu {opcoes[computador]}')
print ('-+' * 30)

if computador == 0 :
	if jogador == 1:
		print('JOGADOR GANHOU')
	elif jogador == 2 :
		print('COMPUTADOR GANHOU')
	elif jogador == 0 :
		print('EMPATE')
	else :
		print('JOGADA INVALIDA')
elif computador == 1:
	if jogador == 1 :
		print('EMPATE')
	elif jogador == 2 :
		print('JOGADOR GANHOU')
	elif jogador == 0 :
		print('COMPUTADOR GANHOU')
	else :
		print('JOGADA INVALIDA')
elif computador == 2 :
	if jogador == 1 :
		print('COMPUTADOR GANHOU')
	elif jogador == 2 :
		print('EMPATE')
	elif jogador == 0 :
		print('JOGADOR GANHOU')
	else :
		print('JOGADA INVALIDA')