def maior(*num):
    maior = max(num)
    print('Analisando os valores:',end='')
    for n in num :
        print(f'{n} ',end='')
    print(f'\n Foram passados {len(num)} valores')
    print(f'O maior valor foi {maior}')
    print('-=' * 20)


maior(1, 3, 2, 5)
maior(3, 6, 7, 7, 9, 23)
