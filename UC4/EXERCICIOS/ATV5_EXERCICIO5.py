idade = int(input('informe a sua idade: '))

if idade < 4:
    print('Idade Inferior a permitida')

elif idade < 6:
    print('Pré-escola')
    
elif idade < 11:
    print('Ensino Fundamental I')

elif idade < 15:
    print('Ensino Fundamental II')

elif idade < 18:
    print('Ensino Médio')

else:
    print('Educação Superior ou Fora da educação regular')