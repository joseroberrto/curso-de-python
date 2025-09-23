#variavel composta (tupla)
valores = int(input('Digite um número: ')) , int(input('Digite mais um número: ')) , int(input('Digite outro número: ')) , int(input('Digite só mais um número: '))

#usando metodo para mostra vezes 
print('-=-' * 15)
print(f'O número 9 apareceu {valores.count(9)} vezes')

#condicao para nao dar erro o metodo index 
if 3 in valores:
	print(f'O número 3 apareceu na  {valores.index(3) + 1 }° posiçao')
else :
	print('Nao foi digitado 3 entre os valores')

# usando for p/ mostas os pares dentro da tupla	
print('Os valores pares foram ' , end = ' ')
for n in valores :
	if n %2 == 0:
		print(n ,  end= ' ' )
print( f' \n{'-=-' * 15}') #charme 