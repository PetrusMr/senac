lado1 = float(input('Informe o tamanho do lado 1: '))
lado2 = float(input('Informe o tamanho do lado 2: '))
lado3 = float(input('Informe o tamanho do lado 3: '))

if lado1 + lado2 < lado3 and lado1 + lado3 < lado2:

   
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('é um triangulo equilatero')
        
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('é um triangulo isosceles')
     
    else:
        print('é um escaleno')
else:
    print('N é triangulo')
