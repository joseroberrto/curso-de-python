salarioInicial = float(input("Digite o valor do sálario: R$"))

salarioReajuste = salarioInicial *(1 + 0.15) #usando o fator de acrescimo para aplicar 15% de aumento

print(f"O sálario de R${salarioInicial} , com aumento de 15% fica R${salarioReajuste:.2f}")