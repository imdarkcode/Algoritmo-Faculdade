print("==============================")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
media = (nota1 + nota2 + nota3)/3
if media >= 6:
    print("Sua média é " + str(round(media, 2)) + ", você está aprovado")
else:
    print("Sua média é " + str(round(media, 2)) + ", você está reprovado")
print("==============================")