operacao = ""

while operacao != "sair":
    operacao = input("Digite 'soma' para somar, 'multiplicacao' para multiplicar ou 'sair' para encerrar: ").lower()

    if operacao == "soma":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")

    elif operacao == "multiplicacao":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é: {resultado}")

    elif operacao == "sair":
        print("Encerrando a calculadora...")

    else:
        print("Operação inválida. Tente novamente.")

#O laço irá repetir até que seja colocado a operação sair, dentro do laço o usuario pode usar a operação soma ou multiplicação