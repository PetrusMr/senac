cod = []
peso = []
altura = []

while True: 
    entrada_cod = input("Informe seu código ou 0 para sair:")
    if entrada_cod == "0":
        if len(peso) == 0 or len(altura) == 0:
            print("Nenhum dado cadastrado!")
            print("Saindo...")
            break
        else:
            print("MAIOR PESO\nPeso:", max(peso), "- cod:", cod[peso.index(max(peso))])
            print("MENOR PESO\nPeso:", min(peso), "- cod:", cod[peso.index(min(peso))])
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("MAIOR ALTURA\nPeso:", max(altura), "- cod:", cod[altura.index(max(altura))])
            print("MENOR ALTURA\nPeso:", min(altura), "- cod:", cod[altura.index(min(altura))])
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            print("MEDIA")
            print("Peso:", sum(peso)/len(peso))
            print("Altura:", sum(altura)/len(altura))
            break
    else:
        entrada_altura = float(input("Informe sua altura:"))
        entrada_peso = float(input("Informe seu peso:"))

        cod.append(entrada_cod)
        altura.append(entrada_altura)
        peso.append(entrada_peso)
