largura = float(input("Digite a largura,em metros: "))
altura = float(input("Digite a altura,em metros: "))

area = largura * altura

#considerando que para cada 2m² de área são necessário 1l de tinta
quantidadeTinta = area / 2

print(f"Sua parede tem a dimensão {largura} x {altura} e sua área é {area:.2f}m²") #:.2f para formatar o número de casas flutuantes e exibir  apenas 2
print(f"Para pintar essa parede,será necessario {quantidadeTinta:.0f}l de tinta")

