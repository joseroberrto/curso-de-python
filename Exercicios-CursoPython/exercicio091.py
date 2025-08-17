from random import randint
from time import sleep
from operator import itemgetter#modulo para colocar em ordem


jogo = {'Jogador1': randint(1,6) , 'Jogador2':randint(1,6),'Jogador3':randint(1,6) , 'Jogador3':randint(1,6) , 'Jogador4':randint(1,6)}

for k , v in jogo.items():
	print(f'O {k} tirou {v} no dado.')
	sleep(0.5)

ranking = list()
ranking = sorted(jogo.items() , key=itemgetter(1) , reverse = True)#colocando em ordem

print('RANK'.center(20,'='))


for i ,v in enumerate(ranking):
	print(f'{i + 1}° Lugar : {v[0]} com {v[1]}')