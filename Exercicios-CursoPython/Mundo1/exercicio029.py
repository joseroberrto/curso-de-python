velocidade = int(input('A quantos km/h voce dirigiu ?'))

if velocidade > 80:
	print(f'Voce ultrapassou o limite de 80km/h \n Por isso ira receber uma multa de  R$ {(velocidade - 80) * 7}')
else : 
	print('Voce dirigiu dentro do limite , muito bem !')
	