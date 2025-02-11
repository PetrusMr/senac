
# cod dos mouses
id_mouse = []
mouse_esfera = []
mouse_limpeza = []
mouse_troca = []
mouse_quebrado = []


while True:
    cod_mouse = input('Adicione um mouse ou 0 para parar: ')
    print('\n')

    if cod_mouse == '0':
        #quantos mouses tem
        quantidade = len(id_mouse)
        quantidade_esfera = len(mouse_esfera)
        quantidade_limpeza = len(mouse_limpeza)
        quantidade_troca = len(mouse_troca)
        quantidade_quebrado = len(mouse_quebrado)

        # descobrindo a %
        porcentagem_esfera = (quantidade_esfera * 100) / quantidade
        porcentagem_limpeza = (quantidade_limpeza * 100) / quantidade
        porcentagem_troca = (quantidade_troca * 100) / quantidade
        porcentagem_quebrado = (quantidade_quebrado * 100) / quantidade

       
        # exibir

        # quantidade total de mouse
        print(f'Quantidade de mouses: {quantidade}')


        # tabela
        print('{0:<30} {1:>30} {2:>30} '.format('situação', 'Quantidade', 'Percentual'))
        
        # bolinha
        print('{0:<30} {1:>30} {2:>30}'.format('Necessita da esfera',quantidade_esfera, porcentagem_esfera))
        
        # limpeza
        print('{0:<30} {1:>30} {2:>30}'.format('Necessita de limpeza',quantidade_limpeza, porcentagem_limpeza))
   
        # troca
        print('{0:<30} {1:>25} {2:>30}'.format('Necessita troca do cabo ou conector',quantidade_troca, porcentagem_troca))
        
        # quebrado
        print('{0:<30} {1:>30} {2:>30}'.format('Quebrado ou inutilizado',quantidade_quebrado, porcentagem_quebrado))
        




        break
    else:
        id_mouse.append(cod_mouse)
        problema = int(input('Informe o problema \n1-necessita da esfera \n2-Necessidade de limpeza \n3-necessidade de troca de cabo ou conector \n4-quebrado ou inutilizado \nDIgite o numero equivalente: '))
        print('\n')
        
        match problema:
            case 1:
                mouse_esfera.append(cod_mouse)
            
            case 2:
                mouse_limpeza.append(cod_mouse)

            case 3:
                mouse_troca.append(cod_mouse)

            case 4:
                mouse_quebrado.append(cod_mouse)







        



