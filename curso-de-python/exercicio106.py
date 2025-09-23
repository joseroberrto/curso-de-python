#leitor de numero inteirou e real

def leiInt(valor):
    while True:
        try:
            numero =int(input(valor))
        except(ValueError ,TypeError):#especificando o tipo de exceção
            print('Erro.Digite um número inteiro valido')
            continue
        else:
            return numero
        

def leiaFloat(valor):
    while True:
        try:
            numero = float(input(valor))
        except:
            print('Erro.Digite um numero real valido')
            continue
        else:
            return numero
        

numeroInt = leiInt('Digite um numero inteiro: ')
numeroFloat = leiaFloat('Digite um número real: ')

print(f'Você digitou o número inteiro {numeroInt}')
print(f'Você digitou o número real {numeroFloat}')