peso = float(input('Digite seu peso ,em Kg :'))
altura = float(input('Digite sua altura ,em metros : '))
imc = peso / (altura **2)

if imc < 18.50 :
	print(f'Seu{imc :.2f} de imc , esta abaixo do peso')
elif imc > 18.50 and imc <= 25:
	print(f'Voce esta com peso ideal ,com imc de {imc :.2f}')
elif imc >25 and imc <= 30 :
	print(f'Seu imc é de {imc :.2f} , o que indica que esta com sobrepeso')
elif imc > 30 and imc <= 40 :
	print(f'Seu imc é de {imc :.2f} , indicando que esta com obesidade')
else :
	print(f'Seu imc é de {imc :.2f} ,que indica que voce esta com obesidade mórbida ')