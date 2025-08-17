aluno= { }


aluno['nome'] = str(input('Nome:  '))
aluno['media']= float(input(f'Média de {aluno['nome']}:  '))

for v,k in aluno.items():
	print(f'{v} é {k}')
	
		
if aluno['media'] >= 6:
	print('Situacao é igual a aprovado')	
else : 
	print('Situacao é igual a  reprovado')
		

