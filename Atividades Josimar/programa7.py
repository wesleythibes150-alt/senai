quant_pao = float(input("Digite a quantidade de paes: "))
quant_broa = float(input("Digite a quantidade de broas: "))

arrecadado = (quant_pao * 0.12) + (quant_broa * 1.50)
poupança = (arrecadado * 0.10)

print("Total de vendas de pão e bros foi: ",arrecadado)
print("Total de arrecadação para poupança: ",poupança)