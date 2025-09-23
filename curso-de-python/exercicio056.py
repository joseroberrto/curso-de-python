somaidade = 0
velho = 0
totalmulher = 0
idadevelho = ' '
idadevelho = 0

for dados in range(1,5):
	print(f'{ '--' *6 } {dados} ° PESSOA {'--' *6} ')
	nome = str(input('Digite seu nome: ')).strip()
	idade = int(input ('Digite sua idade : '))
	sexo = str(input('Qual seu sexo [F/M]: ')).strip()
	somaidade += idade
	if dados == 1 and sexo in ' Mm ' :
		idadevelho = nome 
		idadevelho = idade
	if sexo in 'Mm' and idade > idadevelho :
		idadevelho = idade
		idadevelho = nome
	if sexo in 'Ff' and idade < 20 :
		totalmulher += 1
print('-×' * 30)

media = somaidade / 4			
print(f'A media das idades do grupo é {media}')
print(f'O mais velho do grupo se chama {idadevelho} e tem {idadevelho} anos')
print(f'O número de mulheres com menos de 20 anos sao {totalmulher}')
	