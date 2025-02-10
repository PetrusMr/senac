vetor_cod = []
vetor_peso = []
vetor_altura = []
cont = 0

while True:
    vetor_cod.append(int(input('Insira o codigo do aluno: ')))
    if vetor_cod[cont] == 0:
        break
    
    cont +=1
    vetor_peso.append(float(input('Insira o peso: ')))
    vetor_altura.append(float(input('Informe a altura: ')))


if len(vetor_peso) == 0 and len(vetor_altura) == 0:
    print(' saindo....')

else:
   
    maximo_peso = max(vetor_peso)
    vet_cod_peso_maior = []

    copia_vetor = vetor_peso.copy()
    copia_codigo = vetor_cod.copy()
    while maximo_peso in copia_vetor:
        contar1 = copia_vetor.index(maximo_peso)
        contar2 = copia_codigo[contar1]
        del copia_vetor[contar1]
        del copia_codigo[contar1]

        vet_cod_peso_maior.append(contar2)

    # menor peso
    minimo_peso = min(vetor_peso)
    vet_cod_peso_menor = []

    del copia_vetor
    del copia_codigo

    copia_vetor = vetor_peso.copy()
    copia_codigo = vetor_cod.copy()
    while minimo_peso in copia_vetor:
        contar1 = copia_vetor.index(minimo_peso)
        contar2 = copia_codigo[contar1]
        del copia_vetor[contar1]
        del copia_codigo[contar1]

        vet_cod_peso_menor.append(contar2)

    minimo_altura = min(vetor_altura)
    vet_cod_altura_menor = []

    del copia_vetor
    del copia_codigo

    copia_vetor_altura = vetor_altura.copy()
    copia_codigo_altura = vetor_cod.copy()

    while minimo_altura in copia_vetor_altura:
        contar1 = copia_vetor_altura.index(minimo_altura)
        contar2 = copia_codigo_altura[contar1]
        del copia_vetor_altura[contar1]
        del copia_codigo_altura[contar1]

        vet_cod_altura_menor.append(contar2)

    maior_altura = max(vetor_altura)
    vet_cod_altura_maior = []

    del copia_vetor_altura
    del copia_codigo_altura

    copia_vetor_altura = vetor_altura.copy()
    copia_codigo_altura = vetor_cod.copy()

    while maior_altura in copia_vetor_altura:
        contar1 = copia_vetor_altura.index(maior_altura)
        contar2 = copia_codigo_altura[contar1]
        del copia_vetor_altura[contar1]
        del copia_codigo_altura[contar1]

        vet_cod_altura_maior.append(contar2)

    media_altura = sum(vetor_altura) / len(vetor_altura) 
    media_peso = sum(vetor_peso) / len(vetor_peso) 
    print(f'\nO maior peso é: {max(vetor_peso)}\nO menor peso é: {min(vetor_peso)}\nA maior altura é: {max(vetor_altura)}\nA menor altura é: {min(vetor_altura)}\nO codigo da(s) pessoa(s) com maior peso: {vet_cod_peso_maior}\nO codigo das pessoas com menor peso: {vet_cod_peso_menor}\nO codigo das pessoas com a maior altura: {vet_cod_altura_maior}\nO codigo das pessoas com a menor altura {vet_cod_altura_menor}\n \na media da altura é :{media_altura}\n a media de peso é de: {media_peso}')
    # tabela

    del vetor_cod[-1]

    print('\n')
    print(f"{'COD':<8}|{'Peso':<8}|{'Altura':<8}")
    print("-" * 26)
    

    for v_c, v_p, v_a in zip(vetor_cod, vetor_peso, vetor_altura):
        print(f"{v_c:<8}|{v_p:<8.2f}|{v_a:<8.2f}")