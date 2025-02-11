salario = float(input('Informe o seu salario: R$'))

if salario <=1000 :
    novo_salario = salario + (salario * 0.2)
    print(f'O salario é de: R${novo_salario}')

elif salario <=3000:
    novo_salario = salario + (salario * 0.15)
    print(f'O salario é de: R${novo_salario}')
else:
    novo_salario = salario + (salario * 0.1)
    print(f'O salario é de: R${novo_salario}')