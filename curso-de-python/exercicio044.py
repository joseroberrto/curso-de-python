print(' [0]Avista \n [1]Avista no Cartao \n [2] 2x no Cartao \n [3] 3x no Cartao')#menu de opções
preço = float(input('Digite o preço do produto: R$ '))
opções = ('Avista' , 'Avista no Cartao' , '2x no Cartao' , '3x no Cartao')
escolido = int(input('Digite o número da opçao escolida :'))

if escolido == 0:
	print(f'Voce pagará R$ {preço * 0.90} , com 10% de desconto')
elif escolido == 1:
	print(f'Voce pagará R${preço * 0.95} , com 5% de desconto!')
elif escolido == 2:
	print(f'Voce pagará R${preço} , sem desconto!')
elif escolido == 3:
	print(f'Voce pagará R${preço *1.20} ,com um juros de  20%!')