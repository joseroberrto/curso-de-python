#Conversor de real para dólar
real = float(input("Quanto de dinheiro você tem na carteira?R$ "))

cotacaoDola = float(input("Qual a cotação atual do dólar? R$ "))

realConvertido = real / cotacaoDola

print(f"Com R${real} você pode comprar US${realConvertido:.2f}")