from random import sample
from time import sleep


print('JOGUE NA MEGA SENA '.center(50, '-'))
banco = list(range(1,61)) #gerando os numeros/ banco de dados
palpites = int(input('Quantos palpites voce quer?'))


for c in range (0 , palpites):
	jogos =sorted(sample(banco, 6))#vai escolher 6 numeros dentro do banco 
	print(f'Jogo {c + 1} : {jogos}')
	sleep(0.5)
	
print('BOA SORTE'.center(50 , '-'))
