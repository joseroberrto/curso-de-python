produtoValorInicial = float(input("Digite o valor do produo: R$"))

produtoValorDesconto = produtoValorInicial *(1 - 0.05) # usando fator de decrecimo para calcular desconto de 5%

print(f"O peoduto que custava R${produtoValorInicial} , com desconto de 5% fica R${produtoValorDesconto:.2f}")