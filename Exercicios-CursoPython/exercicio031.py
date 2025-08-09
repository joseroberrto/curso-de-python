distancia = float(input('Digite a distancia , em Km , de sua viagem : '))

if distancia <= 200 :
	print(f'Com a distancia de {distancia}km \n Voce pagará de passagem R$ {distancia *0.50:.2f}')
else :
	print(f'Com a distancia de {distancia } km \n Voce pagará de passagem R$ {distancia * 0.45 :.2f}' )
print('Boa viagem !!')