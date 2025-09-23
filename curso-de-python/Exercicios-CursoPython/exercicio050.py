soma = 0
for n in range(1,7):
	numero = int(input('Digite um número : '))
	if numero %2 ==0 :
		soma += numero

print('+-' * 30)
print(f'A soma dos numeros pares digitados é {soma}')
print('+-' * 30 )