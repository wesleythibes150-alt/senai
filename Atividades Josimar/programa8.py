nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade < 0 or idade > 120:
    print("Idade incorreta! Por favor, digite um valor menor ou igual a 120")

dias_de_vida = idade * 365
print("Você ja viveu",dias_de_vida,"da sua vida")
