nota1 = float(input('Dugite sua primeira nota :'))
nota2= float(input('Digite sua segunda nota :'))
media = (nota1 + nota2 ) / 2

if media < 5.0 :
	print('Poxa , sua média foi abaixo do limite , voce foi REPROVADO')
elif media > 5.0 and media < 6.9 :
	print('Que pena , voce esta em RECUPERACAO')
else :
	print('Parabens , voce foi APROVADO !!')