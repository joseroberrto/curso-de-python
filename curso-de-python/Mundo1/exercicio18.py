#calculando seno,cosseno e tangente
from math import radians,cos,sin,tan #importando funções trigonometricas da biblioteca

angulo = float(input("Digite o valor do ângulo que deseja:° "))

anguloEmRadianos = radians(angulo)
cosseno = cos(anguloEmRadianos)
seno = sin(anguloEmRadianos)
tangente = tan(anguloEmRadianos)


print(f"O seno do angulo de {angulo}° vale {seno:.2f}°")
print(f"O cosseno do angulo de {angulo}° vale {cosseno:.2f}°")
print(f"A tangente do angulo de {angulo}° vale {tangente:.2f}°")