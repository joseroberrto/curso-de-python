
expressao = str(input('Digite uma expressao: '))#string é uma lista tambem
pilha= []



for digit in expressao:
	if digit == '(':
		pilha.append('(')
	elif digit == ')' :
		if len(pilha) > 0:
			pilha.pop()
		else :
			pilha.append(')')
			break
		
		
		

	
if len(pilha) == 0:
	print('Expresaao valida')
else :
	print('Expresaao invalida')

