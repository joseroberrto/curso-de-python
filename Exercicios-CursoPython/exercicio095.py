#variaveis
geral = list()
dados = dict()
partidas = list()
totgol = 0 ##acumulador 

while True:
    #add nome e quant de partidas jogadas
    dados['nome'] = str(input('Digite seu nome:  ')).strip().capitalize()
    tot= int(input(f'Quantas partidas {dados['nome']} jogou? '))

    #coletando quant de gols em cada partida
    for c in range(0,tot):
        partidas.append(int(input(f'   No jogo {c + 1} marcou quantos gols? ')))

    
    for g in partidas:
        totgol += g

    dados['gols'] = partidas[:]
    dados['totgols'] = totgol
    dados['partidas'] = partidas[:]
    partidas.clear()
    totgol = 0
    geral.append(dados.copy())
    
    while True:
        resp =str(input ('Quer continuar?S/N  ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRRO,RESPOSTA INVALIDA')
   
    if resp == 'N':
        break
print('-=' *20)

print(f'{'Cod.Jog:':<10} {'Jogador':^10} {'TotGol':>10}')
for i,v in enumerate(geral):
    print(f'{i:<10} {v['nome']:^10} {v['totgols']:>10}')

print('-=' *20)
print(f'{'---LEVANTAMENTO---':^10}')
cont = 0
while True:
    resp = int(input('Quer mostrar dados de qual jogador?[999 interrope]'))
    if resp == 999:
        break
    if resp > len(geral):
        print('ERRO.JOGADOR NAO EXISTE')
    if resp <= len(geral):
        print(f'O jogador {geral[resp]['nome']}:')
        for i,g in enumerate(geral[resp]['partidas']):
            print(f'   No jogo {i +1} marcou {g} gols')
        print(f'Ao todo fez {geral[resp]['totgols']} gols')
            
        
print('>>>VOLTE SEMPRE<<<')