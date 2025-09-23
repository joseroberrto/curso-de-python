def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
   
jogador= input('Digite o nome do jogador:')
gol = input('Digite o núnemro de gols : ')
if gol.isnumeric():
    gol = int(gol)
else :
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador,gol)
    