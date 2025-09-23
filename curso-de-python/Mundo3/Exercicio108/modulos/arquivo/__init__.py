from modulos.funcao.utils import cabeçalho


def arquivoExiste(nome):
    try:
        a = open(nome ,'rt')#'rt' para ler e fechar o arquivo
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome ,'wt+')#vai criar um novo arquivo caso não exista
        a.close
    except:
        print('Erro desconhecido ao criar arquivo...')


def lerArquivo(nome):
    try:
        a = open(nome ,'rt')#para ler e fechar o arquivo
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a :
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n' , '')
            print(f'{dados[0]:<30}{dados[1]:>5} anos') 


def cadrastarPessoa(arq , nome='desconhecido' ,idade=0):
    try:
        with open(arq ,'a') as c:
            c.write(f'\n{nome};{idade}')
        print(f'Novo registro de {nome} adicionado')
    except:
        print('Erro ao cadastrar nova pessoa')
    