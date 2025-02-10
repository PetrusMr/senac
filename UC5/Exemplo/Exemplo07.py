from customtkinter import *

cod = []
peso = []
altura = []

mais_alto = 0
cod_alto = 0

mais_baixo = 0
cod_baixo = 0

mais_pesado = 0
cod_pesado = 0

mais_leve = 0
cod_leve = 0

media_peso = 0
media_altura = 0

def salvar ():
    global cod, peso, altura, mais_alto, cod_alto, cod_baixo, mais_baixo, mais_pesado, cod_pesado, mais_leve, cod_leve, media_altura, media_peso
    try:
        cod_temp = int(entry_cod.get())
        peso_temp = float(entry_peso.get())
        altura_temp = float(entry_altura.get())

        cod.append(cod_temp)
        peso.append(peso_temp)
        altura.append(altura_temp)

        entry_cod.delete(0,END)
        entry_peso.delete(0,END)
        entry_altura.delete(0,END)

        mais_alto = max(altura)
        cod_alto = cod[altura.index(max(altura))]

        mais_baixo = min(altura)
        cod_baixo = cod[altura.index(min(altura))]

        mais_pesado = max(peso)
        cod_pesado = cod[peso.index(max(peso))]

        mais_leve = min(peso)
        cod_leve = cod[peso.index(min(peso))]

        media_altura = sum(altura)/len(altura)
        media_peso =  sum(peso)/len(peso)
    except ValueError:
        return

    

def resultado ():
    global cod, peso, altura, mais_alto, cod_alto, cod_baixo, mais_baixo, mais_pesado, cod_pesado, mais_leve, cod_leve, media_altura, media_peso
    


    root_resultado = CTkToplevel(master = root)
    root_resultado.title('Resultado')
    root_resultado.attributes('-topmost', True)

    lb_titulo_resultado =  CTkLabel(master=root_resultado, text='Resultado', font=('Arial', 30))
    lb_titulo_resultado.grid(row=0, column=1,ipadx =30, ipady=10, padx= 40)

    lb_cod_resultado = CTkLabel(master=root_resultado, text='Codigo', font=('Arial', 20))
    lb_cod_resultado.grid(row= 1, column= 2)

    
    lb_valor_resultado = CTkLabel(master=root_resultado, text='valor', font=('Arial', 20))
    lb_valor_resultado.grid(row= 1, column= 3, padx= 50)

    #altura
    lb_mais_alto = CTkLabel(master=root_resultado, text='Mais Alto', font=('Arial', 20))
    lb_mais_alto.grid(row=2, column= 0, padx=10, sticky='w')

    lb_mais_baixo = CTkLabel(master=root_resultado, text='Mais Baixo', font=('Arial', 20))
    lb_mais_baixo.grid(row=3, column= 0, padx=10, sticky='w')


    lb_espaço = CTkLabel(master=root_resultado, text='')
    lb_espaço.grid(row=4, column = 0, pady=30)

    #peso
    lb_mais_pesado = CTkLabel(master=root_resultado, text='Mais Pesado', font=('Arial', 20))
    lb_mais_pesado.grid(row=5, column= 0, padx=10, sticky='w')

    lb_mais_leve = CTkLabel(master=root_resultado, text='Mais Leve', font=('Arial', 20))
    lb_mais_leve.grid(row=6, column= 0, padx=10, sticky='w')

    lb_espaço2 = CTkLabel(master=root_resultado, text='')
    lb_espaço2.grid(row=7, column=0,)



    lb_media_peso = CTkLabel(master=root_resultado, text= 'Media de peso', font=('Arial', 20))
    lb_media_peso.grid(row=8, column = 0,  padx=10, sticky='w')

    lb_media_altura = CTkLabel(master=root_resultado, text= 'Media de altura', font=('Arial', 20))
    lb_media_altura.grid(row=9, column = 0,  padx=10, sticky='w')


    entry_cod_resultado_alto = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_cod_resultado_alto.grid(row=2, column = 2)

    entry_valor_resultado_alto = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_valor_resultado_alto.grid(row=2, column = 3)

    entry_cod_resultado_baixo = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_cod_resultado_baixo.grid(row=3, column = 2)

    entry_valor_resultado_baixo = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_valor_resultado_baixo.grid(row=3, column = 3)




    entry_cod_resultado_gordo = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_cod_resultado_gordo.grid(row=5, column = 2)

    entry_valor_resultado_gordo = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_valor_resultado_gordo.grid(row=5, column = 3)

    entry_cod_resultado_magro = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_cod_resultado_magro.grid(row=6, column = 2)

    entry_valor_resultado_magro = CTkEntry(master=root_resultado, width=70,border_color='#af2727', corner_radius=32)
    entry_valor_resultado_magro.grid(row=6, column = 3)


    entry_media_peso = CTkEntry(master=root_resultado,width=70,border_color='#af2727', corner_radius=32 )
    entry_media_peso.grid(row=8, column=1)

    entry_media_altura= CTkEntry(master=root_resultado,width=70,border_color='#af2727', corner_radius=32 )
    entry_media_altura.grid(row=9, column=1)
   
    entry_valor_resultado_alto.insert(0,f'{mais_alto}')
    entry_cod_resultado_alto.insert(0,f'{cod_alto}')

    

    entry_valor_resultado_baixo.insert(0,f'{mais_baixo}')
    entry_cod_resultado_baixo.insert(0,f'{cod_baixo}')


    entry_valor_resultado_gordo.insert(0,f'{mais_pesado}')
    entry_cod_resultado_gordo.insert(0,f'{cod_pesado}')



    entry_valor_resultado_magro.insert(0,f'{mais_leve}')
    entry_cod_resultado_magro.insert(0,f'{cod_leve}')


    entry_media_altura.insert(0,f'{media_altura:.2f}')
    entry_media_peso.insert(0,f'{media_peso:.2f}')


    entry_media_altura.configure(state="disabled")
    entry_media_peso.configure(state="disabled")

    entry_valor_resultado_magro.configure(state="disabled")
    entry_cod_resultado_magro.configure(state="disabled")

    entry_valor_resultado_gordo.configure(state="disabled")
    entry_cod_resultado_gordo.configure(state="disabled")   

    entry_valor_resultado_baixo.configure(state="disabled")
    entry_cod_resultado_baixo.configure(state="disabled")

    entry_valor_resultado_alto.configure(state="disabled")
    entry_cod_resultado_alto.configure(state="disabled")

root = CTk()
root.title('Cadrastro')
lb_titulo = CTkLabel(master=root, text='Cadrastro', font=('Arial', 30))
lb_titulo.grid(row=0, column=1,ipadx =30, ipady=10, padx= 40)

lb_cod = CTkLabel(master=root, text='cod:',font=('Arial', 20))
lb_cod.grid(row=1, column =0, padx=10, pady  = 50)

entry_cod = CTkEntry(master=root,width= 100,border_color='#af2727', corner_radius=32 )
entry_cod.grid(row=1, column=2, pady = 50,padx = 20)



lb_peso = CTkLabel(master=root, text='Peso: ', font=('Arial', 20) )
lb_peso.grid(row=2, column= 0, padx=40, )

entry_peso = CTkEntry(master=root,width= 100,border_color='#af2727', corner_radius=32 )
entry_peso.grid(row =2, column = 2, padx = 20)


lb_altura = CTkLabel(master=root, text='Altura: ', font=('Arial', 20),)
lb_altura.grid(row= 3, column= 0, padx=10, pady = 20)

entry_altura = CTkEntry(master=root, width= 100, border_color='#af2727', corner_radius=32)
entry_altura.grid(row=3, column = 2, pady=20, padx = 20)

btn_salvar = CTkButton(master=root, text='Salvar',font=('Arial', 15) ,command=salvar, fg_color='#ff3535', hover_color='#af2727', corner_radius=32)
btn_salvar.grid(row=4, column=1)

btn_resultado = CTkButton(master=root, text='Resultado',font=('Arial', 15) , command=resultado, fg_color='#ff3535', hover_color='#af2727', corner_radius=32)
btn_resultado.grid(row=5, column=1, pady= 20)

root.mainloop()