def soma():
    resultado = nm1 + nm2
    return print(f'Resultado {resultado}')
def subtração():
    resultado = nm1 - nm2
    return print(f'Resultado {resultado}')
def multiplicação():
    resultado = nm1 * nm2
    return print(f'Resultado {resultado}')
def divisão():
    resultado = nm1 / nm2
    return print(f'Resultado {resultado}')

while True:
    nm1 = int(input('Informe o primeiro numero: '))
    nm2 = int(input('Informe o segundo numero: '))

    escolha = str(input('Escolha uma opção: \n1- Soma \n2-Subtração \n3-Multiplicação \n4-Divisão \n5-Todas as anteriores \n0-Sair\n'))

    match escolha:
        case '1':
            soma()
        case '2':
            subtração()
        case '3':
            multiplicação()
        case '4':
            divisão()
        case '5':
            soma()
            subtração()
            multiplicação()
            divisão()
        case '0':
            print('saindo')
            break
        case _:
            print('Opção Invalido')