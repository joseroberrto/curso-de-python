nome_completo = str(input("Digite seu nome completo :")).strip()
dividido = nome_completo.split()

print(f'Seu primeiro nome é {dividido[0]}')#imprime a parte splitada do nome_comleto onde estar o primeiro nome
print(f'Seu ultimo nome é {dividido[len(dividido)-1]}')