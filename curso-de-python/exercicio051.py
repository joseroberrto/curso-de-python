print('=' * 30)#linha divisoria
print('10 TERMOS DE UMA P.A')
print('=' * 30)

a1 = int(input('Digite o primeiro termo da P.A : '))
r = int(input('Digite o valor da razao : '))
an = a1 + (10 - 1) * r #formula matematica do termo geral de uma P.A

for p in range(a1 , an + 1 , r):
	print(f'{p} ' , end = '-> ')
print('FIM')
	