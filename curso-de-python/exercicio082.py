#variaveis
listnum = []
listpares=[]
listimpar=[]


#loop para digitar N numeros
while True :
	listnum.append(int(input('Digite um número:  ')))
	resp = str(input('Quer continuar?[S/N]  ')).strip()
	print('-=-' * 20)
	
	while resp not in 'NnSs':#vericaçao 
		resp = str(input('Digite novamente.Quer continuar?[S/N]  ')).strip()
		
	if resp in 'Nn':#condicao de parada 
		print('-=-' * 20)
		break
		
		

#para separar numeros impares e pares 
for elem in listnum:
	if elem %2 == 0 or elem==2:
		listpares.append(elem)
	else:
		listimpar.append(elem)

#saída com tres listas : pares ,impares , todas
print(f'Voce digitou: {listnum}')
print(f'Os números pares foram: {listpares}')
print(f'Os números imapres foram: {listimpar}')