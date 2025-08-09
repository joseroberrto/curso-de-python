from time import sleep
#Programa Tabuada
print('=' *30)#linha divisoria
print('\033[1mTABUADA AUTOMÁTICA\033[m')#titulo colorido com ASCII
print('=' *30)

nun = int(input('Digite qual número quer sua tabuada : '))
print('--' * 20)#linha divisoria

for c in range (1 , 11):
		sleep(0.2)
		print(f' {nun}  × {c:2} = {nun*c:1}')#:2 serve pra alinha (2 casas)
print('--' * 20)