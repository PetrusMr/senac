vetor_peso = []
vetor_altura = []
vetor_code = []
while True :
    codigo = input("informe o codigo ou 0 para sair: ")

    match codigo :
        case "0":
            media = len(vetor_altura)
            peso_maior = max(vetor_peso)
            peso_menor = min(vetor_peso)
            alt_maior = max(vetor_altura)
            alt_menor = min(vetor_altura)
            soma_altura = sum(vetor_altura)
            soma_peso = sum(vetor_peso)
            vetor_code_peso_max = vetor_peso.index(max(vetor_peso))
            vetor_code_peso_min = vetor_peso.index(min(vetor_peso))
            vetor_code_alt_max = vetor_altura.index(max(vetor_altura))
            vetor_code_alt_min = vetor_altura.index(min(vetor_altura))
            media_altura = soma_altura / media
            media_peso = soma_peso / media

            peso_code_max = vetor_code[vetor_code_peso_max]
            peso_code_min = vetor_code[vetor_code_peso_min]
            alt_code_max = vetor_code[vetor_code_alt_max]
            alt_code_min = vetor_code[vetor_code_alt_min]

            break

        case _:
            vetor_code.append(codigo)
            altura = float(input("informe a altura: "))
            peso = float(input("informe o peso: "))
            vetor_peso.append(peso)
            vetor_altura.append(altura)

print("\n Resultado do senso")
print(f"codigo:{alt_code_max} mais alto:{alt_maior} ")
print(f"codigo:{alt_code_min} mais baixo:{alt_menor}")
print(f"codigo:{peso_code_max} mais gordo:{peso_maior} ")
print(f"codigo:{peso_code_min} mais magro:{peso_menor} ")
print(f"media de altura:{media_altura} ")
print(f"media de peso:{media_peso} ")



