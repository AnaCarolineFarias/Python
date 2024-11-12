np1 = float(input("Digite sua primeira nota: "))
np2 = float(input("Digite sua segunda nota: "))
pim = float(input("Digite sua nota do PIM: "))

media = ((np1 * 4) + (np2 * 4) + (pim * 2)) / 10

print("Sua média foi de: {:.1f}".format(media))

if media >= 7.0:
    print("Aprovado(a)!")
else:
    print("Reprovado(a)! Faça o Exame!")

exame = float(input("Digite a nota do exame: "))
media_final = (media + exame) / 2

print("Sua média final após o exame foi de: {:.1f}".format(media_final))

if media_final >= 5.0:
    print("Aprovado(a) após o exame!")
else:
    print("Reprovado(a) mesmo após o exame.")
