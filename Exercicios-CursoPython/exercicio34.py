#salario com aumento
salario = float(input('Digite o valor do seu sálario :'))

if salario > 1250 :
	print(f'Com o reajuste , seu novo sálario é R$ {salario * 1.1 :.2f}')
else :
	print(f'Com o reajuste ,seu novo sálario é R$ {salario *1.15 :.2f}')