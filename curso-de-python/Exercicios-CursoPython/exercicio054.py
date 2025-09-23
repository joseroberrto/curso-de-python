from datetime import date
#Cadrasto de pessoas e seus respectivos anos de nascimento
totmaior = 0
totmenor = 0

for pess in range(1,8):
	nasc = int(input(f'Em que ano a {pess} ° pessoa nasceu ?  '))
	idade = date.today().year - nasc
	if idade >= 21:
		totmaior = totmaior + 1
	else :
		totmenor = totmenor + 1

#Saida com analise de dados obtidos
print(f'O número de pessoas com a maioridade é {totmaior}') 
print(f'E os que ainda nao atingiram são {totmenor}')