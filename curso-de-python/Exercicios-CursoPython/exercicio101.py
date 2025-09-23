
def voto(nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 16:
        return str(f'Com {idade} anos :Voto NEGADO')
    if 16 <= idade < 18 or idade >= 65:
        return str(f'Com {idade} anos : Voto OPTATIVO')
    else:
       return str(f'Com {idade} anos : Voto OBRIGATORIO')


ano = int(input('Em qual ano você nasceu?  '))
print(voto(ano))