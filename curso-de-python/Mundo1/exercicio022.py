nome = input("Digite seu nome completo :")

#Metodos de manipulação de strings 
maiúsculo = nome.upper()
minusculo = nome.lower()
dividido = nome.split()
junto = ''.join(dividido)

#saídas
print("-" * 50) #linha divisoria
print(f'Nome em maiúsculo é {maiúsculo}')
print(f'Nome em minusculo é {minusculo} ')
print(f'O número de letras do nome é {len(junto)}') 
print(f'O número de letras do primeito nome é {len(dividido[0])}')#p/ contar o número de letras do 1° nome/parte splitada
print("-" * 50)