nm = int(input('Informe o numero: '))

if nm > 0:
    for c in range(1,10+1):
        tabuada = c * nm
        print(f'{c} * {nm} = {tabuada}')

else:
    print('Numero n positivo')