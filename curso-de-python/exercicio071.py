valor = int(input('Qual o valor a ser sacado? R$  '))
cédula = 50
total = valor
totalcédula = 0
while True:
	if total >= cédula :
		total -= cédula 
		totalcédula += 1
	else :
		if totalcédula > 0 :
			print(f'São {totalcédula} notas de R$ {cédula}')
		if cédula == 50:
			cédula = 20
		elif cédula == 20 :
			cédula = 10
		elif cédula == 10 :
			cédula = 1
		totalcédula = 0
		if total == 0:
			break
