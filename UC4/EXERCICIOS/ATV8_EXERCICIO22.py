
# vetores 
id_mouse = []
mouse_esfera = []
mouse_limpeza = []
mouse_troca = []
mouse_quebrado = []
mais_q_1_problema = []


while True:
    cod_mouse = input('Adicione um mouse ou 0 para parar: ')
    print('\n')

    if cod_mouse == '0':
        if id_mouse:
        
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
            print('\n')

            # tabela
            print('{0:<30} {1:>30} {2:>30}'.format('situação', 'Quantidade', 'Percentual'))
            
            # bolinha
            print('{0:<30} {1:>30} {2:>30} {3:<2}'.format('Necessita da esfera',quantidade_esfera, porcentagem_esfera, '%'))
            
            # limpeza
            print('{0:<30} {1:>30} {2:>30} {3:<2}'.format('Necessita de limpeza',quantidade_limpeza, porcentagem_limpeza, '%'))
    
            # troca
            print('{0:<30} {1:>25} {2:>30} {3:<2}'.format('Necessita troca do cabo ou conector',quantidade_troca, porcentagem_troca, '%'))
            
            # quebrado
            print('{0:<30} {1:>30} {2:>30} {3:<2}'.format('Quebrado ou inutilizado',quantidade_quebrado, porcentagem_quebrado, '%'))
            

        # confirmação se houver mais de 1 problema
        
            # esse if so vai acontecer se tivel algo dentro do vetor
            if mais_q_1_problema:
                print('\n')
                confirmacao_de_relatorio_profundo = str(input('Tem mouses que contém mais de 1 problema, deseja ver quais? (Responda "sim" ou "nao"): ')).lower()
                
                #exibe os problemas
                if confirmacao_de_relatorio_profundo =='sim':
                    print('\n')
                    
                    # contando quantos mouses tem problema
                    print(f'São {len(mais_q_1_problema)} mouses que contem mais de 1 problema, sendo eles: ')
                    
                    # ordenando de menor para maior
                    mais_q_1_problema.sort()
                    print(mais_q_1_problema)
                    
                    
                    break
            
                # confirmar caso n queira ver
                elif confirmacao_de_relatorio_profundo == 'nao' or confirmacao_de_relatorio_profundo == 'não':
                    break
                
                # n digitou oq foi informado
                else:
                    print('erro de confirmação')
                break
            
            #  caso o vetor mais_q_1_problema esteja vazio la em cima ele pula para ca
            else:
                break  
        else:
            print('Não informou nenhum mouse')
            break
    else:
        
        # verifica se o id do mouse ja foi adicionado anteriormente
        if cod_mouse in id_mouse:
            confirmacao_de_id_repetida = str(input('O mouse infrormado ja foi cadrastrado, ele contém mais algum problema? (Responda "sim" ou "nao"): ')).lower()
            print('\n')
            if confirmacao_de_id_repetida == 'sim':
                mais_q_1_problema.append(cod_mouse)
                
            elif confirmacao_de_id_repetida =='nao' or confirmacao_de_id_repetida == 'não':
                exit
                
            else:
                print('erro de confirmação')
                
            
        
        else:
            id_mouse.append(cod_mouse)
            problema = int(input('Informe o problema: \n1-necessita da esfera \n2-Necessidade de limpeza \n3-necessidade de troca de cabo ou conector \n4-quebrado ou inutilizado \nDIgite o numero equivalente: '))
            print('\n')
            
            # casos para funcionar
            match problema:
                case 1:
                    mouse_esfera.append(cod_mouse)
                
                case 2:
                    mouse_limpeza.append(cod_mouse)

                case 3:
                    mouse_troca.append(cod_mouse)

                case 4:
                    mouse_quebrado.append(cod_mouse)

                case _:
                    print('Não corresponde a uma das opções')
                    print('\n')
                    id_mouse.remove(cod_mouse)






        



