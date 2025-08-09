
dados = [ ]

while True:
	nome = input('Nome:  ')
	nota1 = float(input('Nota 1:  '))
	nota2 = float(input('Nota 2:  '))
	media = (nota1 + nota2)/2 
	resp = str(input('Quer continuar?[S/N]  '))
	print('-=-' * 20)
	
	dados.append([nome ,[nota1 , nota2] , media ])
	
	if resp in 'Nn':
		break

print('BOLETIM GERAL'.center(30,'='))
print(f'{"No.":<10}{"Nome":^10}{"Media":>10}')

for i , n in enumerate(dados):
	print(f'{i:<10} {n[0]:^10} {n[2]:>15.1f}')
	



while True:
	r = int(input('Mostrar a nota de qual aluno?(999 interomper)   '))
	if r == 999:
		print('Finalizando...')
		break
	if r <= (len(dados) - 1):
		print(f'O aluno {dados[r][0] } , teve as notas  {dados[r][1]}')
	print('-=-' * 20)
print('Volte Sempre'.center(30 , '='))
	

	
		