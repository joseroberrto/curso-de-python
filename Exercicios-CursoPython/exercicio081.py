
listnum=[]
cont= 0
for cont in range (0,5):
	listnum.append( int(input('Digite um número: ')))
	cont +=1	
listnum.reverse()
	
print(f'Foram digitados {cont} elementos')
print(f'Os numeros em ordem decrescente : {listnum}')

#condicao p/ 5 se estiver na lista 
if 5 in listnum:
	for i , v in enumerate(listnum):#mostra o indice de X vezes que 5 apareceu
		if v == 5 :
			print(f'5 foi digitado na lista ,na posicao {i + 1}')	
else : 
	print('5 nao encontrado')