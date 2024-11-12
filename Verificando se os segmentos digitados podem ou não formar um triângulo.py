print("\033[0;31;40m-=\033[m" * 20)
print("\033[0;34;40mAnalisador de Triângulos\033[m")
print("\033[0;31;40m-=\033[m" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\n Os segmentos acima \033[0;32;40mPODEM FORMAR\033[m um triângulo!")
else:
    print("Os segmentos acima \033[0;31;40mNÃO PODEM FORMAR\033[m um triângulo!")

print("\033[0;31;40m-=\033[m" * 20)
