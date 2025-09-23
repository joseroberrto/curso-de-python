
numero = somanumero =totalnumero = maiornumero = menornumero = 0
resp = 'S'

while resp in 'Ss':
	numero = int(input('Digite um valor :  '))
	somanumero += numero # somador 
	totalnumero += 1 # contador 
	if totalnumero == 1:
		maiornumero = menornumero = numero
	else :
		if numero > maiornumero :
			maiornumero = numero
		if numero < menornumero:
			menornumero = numero
	resp = str(input('Quer continuar ? [S/N]    ')).strip()
	
#fim do programa e charme
print('-=-' * 20)	
print(f'A média entre os valores digitados é {somanumero / totalnumero}')
print (f'E o maior número foi {maiornumero} e o menor foi {menornumero}')
print('-=-' * 20)

