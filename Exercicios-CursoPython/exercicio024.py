#variaveis 
nun = int(input("Digite um numero :"))
u = nun//1 %10 # meio matemático para saber quantidade de unidades
d = nun//10 %10 # meio matemático para saber quantidade de dezenas
c = nun//100 %10# meio matemático para saber quantidade de centenas
m = nun//1000 % 10# meio matemático para saber quantidade de nilhares

#Saída do programa
print(f'O numero de milhar é      {m}')
print(f'O numero de centenas é {c}')
print(f'O numero de dezenas é   {d}')
print(f'O numero de unidades é  {u}')