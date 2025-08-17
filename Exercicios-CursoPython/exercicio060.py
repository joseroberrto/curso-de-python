from math import factorial
numero = int (input('Digite um numero p/ ver seu fatorial :  '))
c = 1# diminuidor 
f = factorial(numero)#metodo para calculo de fatorial
print(f'{numero}! = {numero} ×', end=' ') # para colocar N! antes de entrar no laço

#repeticao ate nunmmero chegar em 1 
while numero > 1 :
	numero = numero - c # vai diminuir o nun de 1 em 1
	print(f'{numero}' , end = ' ' )
	if numero > 1 :
		print('×' , end = ' ')# vai dar o visuap n × n
	else :
		print (f'= {f} ' , end= " "  )