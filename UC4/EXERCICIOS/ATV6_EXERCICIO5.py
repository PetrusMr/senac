nm = int(input('Informe o valor: '))
fatorial = 1

if nm >= 0:

    for c in range(nm, 0, -1):
        fatorial = fatorial * c


    print(f'O fatorial de {nm} é: {fatorial}') 

else:
    print('N é fatoriavel!')