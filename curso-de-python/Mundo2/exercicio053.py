frase = str(input('Digite uma frase : ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inversor= ' '

for letra in range(len(junto) - 1 , -1 , -1 ) :
	inversor = inversor + junto[letra]
	
print(inversor)
print()