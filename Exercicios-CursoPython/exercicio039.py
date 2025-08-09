from datetime import date
nascimento = int(input("Digite o ano de seu nascimento :"))
idade = date.today().year - nascimento

if idade ==18 :
	print('Ta na hora de se alistar , o alistamento é OBRIGATORIO')
elif idade > 18 :
	print(f'O tempo do alistamento ja passou em {idade - 18} anos , se ainda nao se alistou ainda dar tempo!')
else :
	print(f'Que sorte ,ainda faltam {18 - idade } anos para seu alistamento \n OBRIGATORIO')
	
