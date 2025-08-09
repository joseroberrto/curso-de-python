cont = somanumero = 0
while True :
	print('-=-' * 20)
	numero = int(input('Digite um número (999 para parar) :  '))
	if numero == 999 :
		break
	cont += 1
	somanumero += numero

print('-×' * 20)
print(f'\033[32mO total de números digitados foi {cont} \nE a soma entre eles é igual a {somanumero} \033[m')#saida colorida com ASCII
print('-×' * 20)