import datetime

nome = input("Qual o seu nome? ")
nascimento = input("Quando que você nasceu? (dd/mm/aaaa): ")
data_nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
data_formatada = data_nascimento.strftime("%d/%m/%Y")

print(f"Olá, {nome}! Você nasceu em {data_formatada}, certo?")
