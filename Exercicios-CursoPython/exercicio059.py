from time import sleep
#Programa de comparação de números e operaçoes aritmeticas
valor01 = int(input('Primeiro valor:  '))
valor02 = int(input('Segunro valor:  '))
opcoes = 0
  
  
while opcoes != 5 :
	print('=-=' * 20)
	print(' [1] Soma \n [2]Multiplicar \n [3]Maior \n [4]Novos numeros \n [5]Sair do programa' )#menu de opcoes para executar
	opcoes = int(input('>>>> Escolha a sua opçao:  '))
	if opcoes == 1:
		soma = valor01 + valor02
		print(f'\033[32m A soma entre {valor01} e {valor02} é {soma} \033[m')
	elif opcoes == 2 :
		produto = valor01 * valor02
		print(f'\033[32m O produto entre {valor01} e {valor02} é {produto} \033[m')
	elif opcoes == 3:
		if valor01 > valor02:
			print(f' \033[32m {valor01} é maior que {valor02} \033[m')
		else :
			print(f' \033[32m {valor02} é maior que {valor01} \033[m ')
	elif opcoes == 4 :
		valor01 = int(input('Primeiro valor:  '))
		valor02 = int(input('Segundo valor:  '))
	else : 
		print('\033[31m Opçao invalida.Tente novamente \033[m')

sleep(1)
print('Finalizando programa....')
sleep(1)
print('Volte Sempre !')