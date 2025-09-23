#conversor de medidas
medidaMetro = float(input("Digite o valor da medida,em metros: "))

medidaKM = medidaMetro / 1000
medidaHM =  medidaMetro / 100
medidaDAM = medidaMetro /10
medidaDM =  medidaMetro * 10
medidaCM =  medidaMetro * 100
medidaMM =  medidaMetro * 1000

print(f"Convertendo a medida {medidaMetro}m: ")
print(f"{medidaMetro}m equivalente a {medidaKM}km")
print(f"{medidaMetro}m equivalente a {medidaHM}hm")
print(f"{medidaMetro}m equivalente a {medidaDAM}dam")
print(f"{medidaMetro}m equivalente a {medidaDM}dm")
print(f"{medidaMetro}m equivalente a {medidaCM}cm")
print(f"{medidaMetro}m equivalente a {medidaMM}mm")