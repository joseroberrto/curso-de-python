maior = 0
menor = 0

for p in range (1, 6):
	peso = float(input(f'Digite o peso da {p}° pessoa , em Kg :   '))
	if p == 1 :#vai ser usado como refencia o peso da pessoa 1
		maior = peso
		menor = peso
	else : #comparacao com a referencia 
		if peso > maior:
			maior = peso # peso lido maior do que a pessoa 1 ele passa a ser a referencia
		if peso < menor : # peso lido menor que a a pessoa 1 ele passar a ser a referencia
			menor = peso

#Saida com analise de dados obtidos
print (f'O maior peso lido foi {maior} Kg')
print (f'O menor peso lido foi {menor} Kg ')