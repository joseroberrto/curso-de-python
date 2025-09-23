#Variavies 
tothomem = 0
maioridade =0
menormulher = 0

while True :
	titulo = 'CADASTRE UMA PESSOA'
	print(f'{titulo :-^50}')
	idade = int(input('Idade:  '))
	sexo = str(input('Sexo [M/F]:   ')).strip().upper().upper()[0]
	
	while sexo not in 'FM' :#verificacao caso usuario nao digite F/M
		sexo = str(input('Digite novamente \nSexo [M/F] :   ')).strip().upper()[0]
		
	if sexo == 'M' :
		tothomem += 1
	if idade > 18 :
		maioridade += 1
	if sexo == 'F' and idade < 20:
		menormulher += 1
	print('--' * 30)
	continua  = input ('Quer continuar ? [S/N]   ').strip().upper()[0]
	if continua == 'N':
		break

#Fim do Programa
print('-=-' * 20)
print(f'No total são {maioridade} pessoas maiores de 18 anos ')
print(f'{tothomem} homens cadastrados')
print(f'E {menormulher} mulheres com idade abaixo de 20 anos ')
print('-=-' * 20)
