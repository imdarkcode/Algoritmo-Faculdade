soma = 0
quantidade = int(input("Informe a quantidade de vendas: "))

for i in range(quantidade):
    venda = float(input("Informe o total da venda: "))
    soma += venda
if soma > 500:
    imposto = soma * 0.15
else:
    imposto = soma * 0.11
print("O imposto será de:",imposto)