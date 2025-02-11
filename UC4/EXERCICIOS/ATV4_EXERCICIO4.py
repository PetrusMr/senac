salario = float(input('Informe o seu salario: R$'))

if salario < 1500:
    salario_novo = salario + (salario * 0.2)
    print(f'Seu salario foi para: R${salario_novo}')

else:
    salario_novo = salario + (salario * 0.1)
    print(f'Seu salario foi para: R${salario_novo}')
