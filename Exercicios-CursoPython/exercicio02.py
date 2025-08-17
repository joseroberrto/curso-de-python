#inversor de frases
frase = str(input("Digite uma frase :")).strip()

#o -1 faz a string andar de traz pra frente ,um caractere por vez 
print(frase[:: - 1])