valorDaCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do seu sálario :R$"))
quantidadeAnos = int(input("Digite a quantidade de anos de financiamento  desejado: "))

prestacao = valorDaCasa / (quantidadeAnos * 12)

valorMinimo = salario * 30/100

print(f"Para pagar a csa no valor R${valorDaCasa} em {quantidadeAnos} anos")
print(f"A prestação será de R${prestacao:.2f}")
if prestacao <= valorMinimo :
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado")

