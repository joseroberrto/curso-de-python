totcompra = 0
maiorpreço =0
cont = 0

while True :
	titulo = 'CAIXA'
	print(f'{titulo :-^40}')
	nome =str(input('Nome:  '))
	preço =int (input('Preço: R$  '))
	cont += 1
	totcompra += preço
	mais = str(input('Quer continuar ? [S/N]   ')).strip().upper()[0]
	if cont == 1 :
		maisbarato = preço
		nomebarato = nome
	else :
			if preço < maisbarato :
				maisbarato = preço
				nomebarato = nome
	if preço > 1000 :
		maiorpreço += 1
	if mais == 'N' :
		break
	
print('-=-' * 20)		
print(f'O total da compra é R$ {totcompra}')
print(f'E são {maiorpreço } produtos acima de R$ 1000')
print(f'O produto mais barato é o {nomebarato } que custa R$ {maisbarato } ')
print('-=-' * 20)
	