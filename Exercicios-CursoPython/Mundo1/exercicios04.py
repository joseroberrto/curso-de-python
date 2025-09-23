##  Dissecando uma Variável 

frase = input("Digite algo:  ")

print("O tipo primitivo é : ",type(frase) )
print("A frase é alfabetica?", frase.isalpha())
print("A frase tem números ? ",frase.isalnum())
print("A frase é alfanúmerica? ",frase.isalnum())
print("A frase tem espaçoes? ",frase.isspace())
print("A frase esta em maiusculas? ",frase.isupper())
print("A frase esta em minusculas? ",frase.islower())
print("A frase esta capitalizada? ",frase.istitle())

