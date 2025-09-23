cores = {'FundoBranco' :'\033[47m ', 'FundoVerde':'\033[42m' , 'Resert' : '\033[0m'}


def ajuda (com):
	print(cores['FundoVerde'])
	help(com)
	print(cores['Resert'])

def titulo (msg , cor=0):
	tam = len(msg)
	print('~' * tam)
	print(msg)
	print('~' * tam)



#Programa Principal
comando = ' '
while True:
	titulo('SISTEMA DE AJUDA PYHELP')
	comando = input('Funcao ou biblioteca > ')
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
	print('ATE LOGO')