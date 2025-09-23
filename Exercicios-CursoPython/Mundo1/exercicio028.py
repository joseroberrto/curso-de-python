from random import randint
#variaveis utilizadas 
numero_sorteado = randint(1,5)
tentativas = 0
escolha = ' '


print ('==' * 16)#Linha divisoria
print('\033[7mADVINHADOR DE NÚMEROS\033[m')#Titulo colorido com ANSI
print('==' * 16)
print('Escolha um número de 1 a 5')

# repetiçao ate o jogador acertar
while escolha != numero_sorteado:
	escolha = int(input('Escolha seu palpite :  '))
	print('\033[31m Que pena ,voce errou :(  \033[m ')#msg de erro colorida com ANSI
	print('--' * 30)
	tentativas += 1 #contador de tentativas
			
#Mostra quantas tentativas até o acerto 		
print('-×' * 21)
print('\033[32mParabens ,voce acertou')#msg de vitória colorida com ANSI
print(f'Voce tentou {tentativas}x até acertar \033[m')
print('-×' * 21)