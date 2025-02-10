nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3) /3

if nota1 < 3 or nota2 < 3 or nota3 < 3:
    print('Reprovado, Umas das notas foi menor que 3')

else:
    if media < 5:
        print('Reprovado')

    elif media < 7:
        print('Recuperação')

    else:
        print('Aprovado')

