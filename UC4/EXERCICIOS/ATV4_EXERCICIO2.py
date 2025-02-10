valor_produto = float(input('Informe o valor do produto: '))



if valor_produto > 100:
    valor_final = valor_produto - (valor_produto * 0.1)
    print(f'Valor do produto é: {valor_final}')
else:
    print(f'O valor do produto é: {valor_produto}')

