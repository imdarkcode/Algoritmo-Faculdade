print("==============================")
cargo = input("Informe seu cargo: ")
nivel = int(input("Informe seu nível de acesso: "))
seguranca = int(input("Informe a segurança: "))

if cargo == "CEO":
    if nivel == 1:
        if seguranca == 0:
            tempo = 166
        else:
            tempo = 150
    else:
        if seguranca > 0:
            tempo = 120
        else:
            tempo = 115
else:
    if nivel > 1:
        tempo = 110
    else:
        tempo = 106

print("O tempo será de " + str(tempo))
print("==============================")