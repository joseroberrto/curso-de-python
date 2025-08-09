primeiro_termo = int (input('Digite o primeiro termo:  '))
razao = int(input('Digite o valor da razao:  '))
termo = primeiro_termo
cont = 1
print('-×' *25)

#repeticao para ter 10 termos da P.A
while cont <= 10 :
	print(f'{termo} --> ' , end = '  ')
	termo += razao
	cont += 1 #contador 
print('Fim')
print('-×' * 25)