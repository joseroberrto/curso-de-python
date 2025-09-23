from math import hypot

catetoOposto = float(input("Digite o valor do cateto oposto: "))
catetoAdjcente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = hypot(catetoOposto ,catetoAdjcente)

print(f"O valor da hipotenusa é {hipotenusa:.2f}")