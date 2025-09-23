diasAlugados = int(input("Digite o número de dias alugados pa o carro: "))
KMrodados = float(input("Digite o número de KM percorridos:"))

precoPorDia = diasAlugados * 60
precoPorKM = KMrodados * 0.60

total = precoPorKM + precoPorDia

print(f"Voce usou o carro por {diasAlugados} dias \n Percorreu {KMrodados} KM \n Total a pagar R${total:.2f}")