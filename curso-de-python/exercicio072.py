exterso = ['zero' , 'um' , 'dois' , 'tres' , 'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez']


while True :
	número = int(input('Digite um número entre 0 e 10:  '))
	if 0 <= número <=10:
		break
	print('Digite novamente.' , end = ' ')
print(f'Voce digitou {exterso[número]} ')