import math
angulo = float(input("Digite o valor do ângulo em graus: "))

angulo_rad = math.radians(angulo)
seno_conta = math.sin(angulo_rad)
cosseno_conta = math.cos(angulo_rad)
tangente_conta = math.tan(angulo_rad)

print("Seno de {}°: {:.2f}".format(angulo,seno_conta))
print("Cosseno de {}°: {:.2f}".format(angulo,cosseno_conta))
print("Tangente de {}°: {:.2f}".format(angulo,tangente_conta))
