primeiro_termo = int(input('Digite o primeiro termo:  '))
razao = int(input('Digite o valor da razao:  '))
termo = primeiro_termo
cont = 1
mais_termos = 10 # ja guarda os 10 primeiros termos
total = 0

while mais_termos  != 0 : # aninhado com os 10 primeiros termos
	total = total + mais_termos # ja comeca com 10
	while cont <= total : # primeiros 10 termos da PA
		print(f'{termo} ->' , end= ' ')
		termo = termo + razao # vai ficar somando com razao
		cont = cont + 1 # contador , a cada repeticao vai contar +1
	print ('Pausa')
	mais_termos = int(input('Quantos termos a mais voce quer ?'))
	
print (f'Progressao finalizada com {total} termos')