nome = input("Insira o nome do aluno :")
nota1 = float(input("Insira a primeira nota :"))
nota2 = float(input("Insira a segunda nota :"))
media = (nota1 + nota2) / 2
print(" A média do aluno é :", media)
if media >= 7:
    print("O aluno está aprovado")
else:
    print("O aluno está reprovado")