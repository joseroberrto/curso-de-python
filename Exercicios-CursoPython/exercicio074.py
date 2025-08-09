from random import randint
#variavel composta (tupla)
números = (randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10) , randint(0,10))

print('Os números sorteados foram :' )
for n in números :#p/ cada elemento n dentro de números
	print(n , end=' ')

print(f'\nO maior número foi {max(números)}')# max e min metodos de tuplas
print(f'O menor número foi {min(números)}')