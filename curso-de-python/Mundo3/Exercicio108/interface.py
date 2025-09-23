from modulos.funcao.utils import*
from modulos.arquivo import*

arquivo = 'sistemacadastro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

linha()
print("SISTEMA DE CADASTROS".center(45))


while True:
    resp = menu(['Cadastrar nova pessoa' ,'Acessar Cadrastros' ,'Sair do Programa'])
    if resp == 1:
        cabeçalho('NOVO CADASTRO')
        pessoa = str(input('Nome: '))
        idade = leiInt('Idade: ')
        cadrastarPessoa(arquivo , pessoa , idade)
    elif resp == 2:
        cabeçalho('CADASTROS REGISTRADOS')
        lerArquivo(arquivo)
    elif resp == 3:
        print('>>Finalizando Programa....')
        print('Até logo')
        break
    else:
        print('Opção Invalida.Tente novamente')





