import datetime
from time import sleep

atual = datetime.date.today().year
dados = {'nome':str(input('Digite seu nome: ')),
         'nascimento': int(input('Digite seu ano de nascimento: ')),
         'ctps':int(input('Digite o nº de sua ctps(0 se não houver);  '))}

dados['idade'] = atual - dados['nascimento']

if dados['ctps'] != 0 :
    dados['salario'] = float(input('Digite o  valor do salário:  '))
    dados['contratação'] = int(input('Digite seu ano de contratação:  '))
    dados['aposentadoria'] =  dados['idade'] + ((dados['contratação'] + 35) - atual)
print('-=' * 20)
for k,v in dados.items():
    print(f'{k} = {v}')  
    sleep(0.5)
