from random import choice
escolha_jogador= str(input('Escolha pedra,papel ou tesoura :')).strip().lower()
lista = [ 'papel' , 'tesoura' , 'pedra' , 'pedra' , 'papel' , 'tesoura']
escolha_pc= choice(lista)

#condição feita para cada possibilidade de escolha do jogador
if escolha_jogador == 'pedra' and escolha_pc== 'papel':
	print(f'O computador escolheu {escolha_pc} e ganhou \n Mais sorte na proxima!')
elif escolha_jogador == 'tesoura' and escolha_pc== 'pedra' :
	print(f'O computador escolheu {escolha_pc} e ganhou \n Mais sorte na proxima!')
elif escolha_jogador == 'papel' and escolha_pc == 'tesoura' :
	print(f'O computador escolheu {escolha_pc} e ganhou \n Mais sorte na proxima!')
elif escolha_jogador =='pedra' and escolha_pc == 'tesoura' :
	print(f'Voce ganhou ! O compuatador escolheu {escolha_pc} e perdeu')
elif escolha_jogador == 'tesoura' and escolha_pc == 'papel' :
	print(f'Voce ganhou ! O computador escolheu {escolha_pc } e perdeu')
elif escolha_jogador == 'papel ' and escolha_pc == 'pedra' :
	print(f'Voce ganhou ! O computador escolheu {escolha_pc} e perdeu')
else :
	print('Deu empate , o computador escolheu o mesmo ')