def contador (i,f,p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if i < f :
        cont = i    
        while cont <= f:
            print(f'{cont}  ',end='')
            cont += p
        print('\n')
    else:
        cont = i
        while cont >= f :
            print(f'{cont}  ',end='')
            cont -= p
        print("\n")
   
#contador(1,10,1)
contador(1,10,1)
print('-=' * 20)
contador(0,10,2)

print('Agora é sua vez de personalizar')
ini = int(input('Inicio: '))
fim = int(input('Final:  '))
pas = int(input('Passo:  '))
contador(ini,fim,pas)