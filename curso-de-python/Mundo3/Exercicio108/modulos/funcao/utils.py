def linha (tam=45):
    print('-' * tam)


def leiInt(valor):
    while True:
        try:
            numero =int(input(valor))
        except(ValueError ,TypeError):#especificando o tipo de exceção
            print('Erro.Digite um número inteiro valido')
            continue
        else:
            return numero
  

def cabeçalho(txt):
    linha()
    print(txt.center(45))
    linha()


def menu(list):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c+=1
    linha()
    opc = leiInt('Sua opção: ')
    return opc

   



