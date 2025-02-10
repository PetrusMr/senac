salario = float(input('Informe o seu salario: R$'))

if salario <= 1900:
    print('Isento de imposto')

elif salario <= 2800:
    Salario_taxado = salario * 0.075
    print(f'Foi descontado de imposto de renda: R${Salario_taxado}')

elif salario <= 3700:
    Salario_taxado = salario * 0.15
    print(f'Foi descontado de imposto de renda: R${Salario_taxado}')

else:
    Salario_taxado = salario * 0.225
    print(f'Foi descontado de imposto de renda: R${Salario_taxado}')