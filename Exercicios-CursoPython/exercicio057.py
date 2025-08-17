sexo = str(input('Informe seu sexo [M/F] : ')).strip().upper()[0]

while sexo not in 'FM':
	sexo = str(input('Dados inavlidos , por favor digite seu sexo [M/F] : ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso')
