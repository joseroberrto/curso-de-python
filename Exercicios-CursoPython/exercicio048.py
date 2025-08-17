soma = 0
cont = 0

for c in range(1 , 501 , 2) :
	if c % 3 == 0 :
		soma = soma + c #acumulador
		cont = cont + 1 #contador
		
print(f'A somatoria entre os {cont} valores é {soma}')
		