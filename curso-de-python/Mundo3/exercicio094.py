pessoa = {}
geral = list()
mulheres = list()
acimamed = list()
totida = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:  '))
    while True:
         pessoa['sexo'] = str(input('Sexo:  ')).upper()
         if pessoa['sexo'] in 'MF':
             break
         print('ERROR.RESPOSTA INVALIDA')
    pessoa['idade'] = int(input('Idade:  '))
    geral.append(pessoa.copy())
    while True:
         resp = str(input('Quer conyinuar?[S/N]  ')).upper()
         if resp in 'SN':
             break
         print('ERRO.RESPOSTA INVALIDA')
    print('-=' * 20)
    if resp == 'N':
        break    
        
for i,v in enumerate(geral):
    totida += v['idade']
    if v['sexo'] == 'F':
        mulheres.append(v['nome'])

media = totida / len(geral)

for i,v in enumerate(geral):
    if v['idade'] > media :
        acimamed.append(v['nome'])
        

print(f'Foram cadastradas {len(geral)} pessoas')
print(f'A média das idades do grupo é {media:.1f} anos')
print(f'Lista de mulheres cadastradas {mulheres}')
print(f'Lista de pessoas acima da media {acimamed}')