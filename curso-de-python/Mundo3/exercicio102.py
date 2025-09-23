
def fatorial(num , show=False):
    """
    -> Calcula Fatorial:
    :param num : recebe o numero a ser calculado
    :param show :(opcional) recebe True ou False para mostra ou não a conta
    :return : retorna o resultado do fatorial calculado de num.
    """
    resultado = 1
    for c in range(num,0,-1):
        if show == True:
            print(f' {c} ',end='')
            if c > 1 :
                print(' x ' , end='')
            else :
                print(' = ' , end='')
        resultado *= c
    return resultado
 
        

#Programa principal
resp = int(input('Digite um número para obter seu fatorial: '))
esco = str(input('True ou False? ')).strip().upper()[0]

if esco in 'True': # conversão de string para valor boleano
    boleano = True
else:
    boleano = False

print(fatorial(resp,boleano))
