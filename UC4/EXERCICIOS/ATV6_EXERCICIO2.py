nm1 = int(input('Informe o primeiro numero inteiro positivo: '))
soma = 0

if nm1 > 0:
    for c in range(1, nm1 + 1):
        soma = soma + c 
    print(soma)
else:
    print('Numero n positivo')
    