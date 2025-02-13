from customtkinter import *

def switch_cadastrar():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_cadastrar.grid(row = 0, column = 1, padx = 5)
    frame_cadastrar.grid_propagate(False)


def switch_editar():
    frame_cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_editar.grid(row = 0, column = 1, padx = 5)
    frame_editar.grid_propagate(False)
 

def switch_saida():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida.grid(row = 0, column = 1, padx = 5)
    frame_saida.grid_propagate(False)

def switch_entrada():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_saida.grid_forget()
    frame_relatorio.grid_forget()
    frame_entrada.grid(row = 0, column = 1, padx = 5)
    frame_entrada.grid_propagate(False)


def switch_relatorio():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_saida.grid_forget()
    frame_entrada.grid_forget()    
    frame_relatorio.grid(row = 0, column = 1, padx = 5)
    frame_relatorio.grid_propagate(False)

root = CTk()
root.geometry('820x400')
root.title('Sistema de gerenciamento')

# frame
frame_lateral = CTkFrame(master=root, width=190, height=390, border_color='#d9d4fd', border_width=2)
frame_lateral.pack_propagate(False)
frame_lateral.grid(row = 0, column = 0, padx=10)

frame_cadastrar = CTkFrame(master=root, width= 590, height=390, border_color='#d9d4fd', border_width=2)
frame_cadastrar.grid_propagate(False)


frame_editar = CTkFrame(master=root, width= 590, height=390, border_color='#d9d4fd', border_width=2)
frame_editar.grid_propagate(False)

frame_saida = CTkFrame(master=root, width= 590, height=390, border_color='#d9d4fd', border_width=2)
frame_saida.grid_propagate(False)

frame_entrada = CTkFrame(master=root, width= 590, height=390, border_color='#d9d4fd', border_width=2)
frame_entrada.grid_propagate(False)

frame_relatorio = CTkFrame(master=root, width= 590, height=390, border_color='#d9d4fd', border_width=2)
frame_relatorio.grid_propagate(False)

# frame_lateral widget

#label 
label_nome_sistema = CTkLabel(master=frame_lateral, text='Nome do\n Sistema', font=('Arial', 30))
label_nome_sistema.pack(pady = 30)

#butao
btn_cadastrar = CTkButton(master=frame_lateral, text='Cadastrar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6',command=switch_cadastrar)
btn_cadastrar.pack()

btn_editar = CTkButton(master= frame_lateral, text='Editar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command=switch_editar)
btn_editar.pack(pady = 10)

btn_saida = CTkButton(master=frame_lateral, text='Saida', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command=switch_saida)
btn_saida.pack()

btn_entrada = CTkButton(master=frame_lateral, text='Entrada', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command=switch_entrada)
btn_entrada.pack(pady=10)

btn_relatorio = CTkButton(master=frame_lateral, text='Relatorio', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command=switch_relatorio)
btn_relatorio.pack()


# #frame cadastrar

# label
label_Cadrastro_produto = CTkLabel(master=frame_cadastrar, text='Cadastro de Produto', font=('Arial', 30),)
label_Cadrastro_produto.grid(row = 0, column = 1, pady=30)


label_nome_produto = CTkLabel(master=frame_cadastrar, text='Nome do Produto:', font=('Arial', 15),  )
label_nome_produto.grid(row = 1, column = 0, pady = 10, padx=30, sticky = 'e')

label_preco_produto = CTkLabel(master=frame_cadastrar, text='Preço (R$):', font=('Arial', 15))
label_preco_produto.grid(row = 2, column = 0, pady = 10, padx=30,sticky = 'e')  

label_descricao = CTkLabel(master=frame_cadastrar, text='Descrição:', font=('Arial', 15), )
label_descricao.grid(row = 3, column = 0, pady = 10, padx=30, sticky='ne')

# entry
entry_nome_produto = CTkEntry(master=frame_cadastrar, width=300, placeholder_text='Nome do Produto', corner_radius=32,border_color='#a399f9')
entry_nome_produto.grid(row = 1, column = 1, pady = 10, sticky='w')

entry_preco = CTkEntry(master=frame_cadastrar, width=80, placeholder_text='R$:', corner_radius=32, border_color='#a399f9')
entry_preco.grid(row=2, column=1, sticky='w')

# textbox

descricao_box = CTkTextbox(master=frame_cadastrar, width=300, height=80,border_color='#a399f9', border_width=2, corner_radius=15)
descricao_box.grid(row=3, column=1, sticky='w',pady=12)

# butao

btn_salvar = CTkButton(master=frame_cadastrar, width=80, text='Salvar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_salvar.grid(row=4, column=1, pady=5,sticky='e')


# frame editar

# Label
label_Editar = CTkLabel(master=frame_editar, text='Editar', font=('Arial', 30),)
label_Editar.grid(row = 0, column = 1, pady=30)



# frame saida

# Label
label_Saida = CTkLabel(master=frame_saida, text='Saida', font=('Arial', 30),)
label_Saida.grid(row = 0, column = 1, pady=30)


# frame entrada

# label
label_Entrada = CTkLabel(master=frame_entrada, text='Entrada', font=('Arial', 30),)
label_Entrada.grid(row = 0, column = 1, pady=30)


# frame relatorio

# label
label_Relatorio = CTkLabel(master=frame_relatorio, text='Relatorio', font=('Arial', 30),)
label_Relatorio.grid(row = 0, column = 1, pady=30)


root.mainloop()