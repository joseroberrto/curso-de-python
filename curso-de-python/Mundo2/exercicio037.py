numero = int(input("Digite um nuero inteiro: "))

print("Escolha uma das opções abaixo \n[1] coverter para Binário \n[2] converter para Octal \n[3] converter hexadecimal")

opcao = int(input("Sua opção: "))

if opcao ==1:
    print(f"O numero {numero} para binario é igual a {bin(numero)}")
elif opcao ==2:
    print(f"O número {numero} para Octal é igual a {oct(numero)} ")
elif opcao ==3:
    print(f"O número {numero} para hexadecimal é igual a {hex(numero)}")