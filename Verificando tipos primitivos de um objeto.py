n = input("Digite algo: ")

print("O tipo primitivo desse valor é: ", type(n))
print("Só tem espaços? ", n.isspace())
print("É um valor alfabético? ", n.isalpha())
print("É um valor númerico? ", n.isnumeric())
print("É um valor alfanumérico? ", n.isalnum())
print("Este valor está em maiúsculos?", n.isupper())
print("Está em minúsculas? ", n.islower())
print("Está capitalizada? ", n.istitle())