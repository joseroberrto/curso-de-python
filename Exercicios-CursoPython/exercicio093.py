#variaveis
jogos = list()
dados = dict()
totgol = 0 ##acumulador 

#add nome e quant de partidas jogadas
dados['nome'] = str(input('Digite seu nome:  ')).strip().capitalize()
partidas= int(input('Quantos jogos jogou? '))

#coletando quant de gols em cada partida
for c in range(0,partidas):
    gols = int(input(f'No jogo {c + 1} marcou quantos gols? '))
    jogos.append(gols)
    totgol += gols

#add lista de gols no dicionario
dados['gols'] = jogos[:]
dados['total'] = totgol

print('-=' * 20)#linha divisoria

#mostrando os dados do dicionario
for k,v in dados.items():
    print(f'No campo {k} tem o valor {v}')
    
print('-=' * 20)
print(f'O jogador {dados['nome']} tem {partidas} jogos.')

#mostrando os dados da lista de gols por partidas 
for i,v in enumerate(jogos):
    print(f'No jogo {i + 1} fez {v} gols')
print('-=' * 20)
print(f'Total de {totgol} gols')