from PIL import Image, ImageTk
from customtkinter import *

import os
file_path = os.path.dirname(os.path.realpath(__file__))
image1 = CTkImage(Image.open(fp= "C:/Users/970548/OneDrive - SENAC em Minas - EDU/Documentos/Senac/senac/UC5/projeto01/lixeira.png"), size=(35,35))

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
root.geometry('840x400')
root.title('Sistema de gerenciamento')

# frame
frame_lateral = CTkFrame(master=root, width=190, height=390, border_color='#d9d4fd', border_width=2)
frame_lateral.pack_propagate(False)
frame_lateral.grid(row = 0, column = 0, padx=10)

frame_cadastrar = CTkFrame(master=root, width= 600, height=390, border_color='#d9d4fd', border_width=2)
frame_cadastrar.grid_propagate(False)


frame_editar = CTkFrame(master=root, width= 600, height=390, border_color='#d9d4fd', border_width=2)
frame_editar.grid_propagate(False)

frame_saida = CTkFrame(master=root, width= 600, height=390, border_color='#d9d4fd', border_width=2)
frame_saida.grid_propagate(False)

frame_entrada = CTkFrame(master=root, width= 600, height=390, border_color='#d9d4fd', border_width=2)
frame_entrada.grid_propagate(False)

frame_relatorio = CTkFrame(master=root, width= 600, height=390, border_color='#d9d4fd', border_width=2)
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

descricao_box = CTkTextbox(master=frame_cadastrar, width=300, height=80,border_color='#a399f9', border_width=2, corner_radius=15, scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#6e67a6')
descricao_box.grid(row=3, column=1, sticky='w',pady=12)

# butao

btn_salvar = CTkButton(master=frame_cadastrar, width=80, text='Salvar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_salvar.grid(row=4, column=1, pady=5,sticky='e')


# frame editar

# Label
label_Editar = CTkLabel(master=frame_editar, text='Editar', font=('Arial', 30))
label_Editar.grid(row = 0, column = 0, pady=5, padx= 250,sticky='w',columnspan=4)


#scrollframe
scroll_frame_edit = CTkScrollableFrame(master=frame_editar, corner_radius=32, border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78')
scroll_frame_edit.grid(row= 2, column=0, sticky='w',rowspan = 4, padx= 30)


# entry
entry_busca_edit = CTkEntry(master=frame_editar, placeholder_text='Buscar Produto', width=400, border_color='#a399f9', corner_radius=32)
entry_busca_edit.grid(row=1, column = 0, pady= 5, padx=30, sticky  = 'w',columnspan=3)

entry_nome_edit = CTkEntry(master=frame_editar, placeholder_text='Nome do Produto', width=250, border_color='#a399f9', corner_radius=32)
entry_nome_edit.grid(row=2, column = 1,  sticky  = 'w', pady=5 )

entry_preco_edit = CTkEntry(master=frame_editar, placeholder_text='R$:', width=80, border_color='#a399f9', corner_radius=32)
entry_preco_edit.grid(row=3, column = 1, sticky  = 'nw',)

# textbox
textbox_edit = CTkTextbox(master=frame_editar,height=150, width=280, border_color='#a399f9', border_width=2, corner_radius=15, scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#6e67a6')
textbox_edit.grid(row=4, column = 1, sticky ='w', pady=5,)


# butao 

btn_salvar_edit = CTkButton(master=frame_editar, text= 'Salvar', width=90, corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_salvar_edit.grid(row=5, column=1,pady=5, sticky='e')

btn_excluir_edit = CTkButton(master=frame_editar, text='Excluir', width=90, corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_excluir_edit.grid(row=5, column=1,pady=5, )

btn_cancelar_edit = CTkButton(master=frame_editar, text='Cancelar',width=90, corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_cancelar_edit.grid(row=5, column=1,pady=5, sticky='w')

# # temporario ---------------
nomes = [
    "Sakura",
    "Yuki",
    "Hana",
    "Aiko",
    "Miyuki",
    "Emi",
    "Haruka",
    "Naomi",
    "Reina",
    "Kaori"
]
# #-----------------------------

# checkbox
for item in nomes:
   box = CTkCheckBox(master=scroll_frame_edit, text=item, corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6', )
   box.pack(pady=5, padx=10, fill="x")




# frame saida

# Label
label_Saida = CTkLabel(master=frame_saida, text='Saida de Produto', font=('Arial', 20),)
label_Saida.grid(row = 0, column = 0, pady=5, padx= 200,sticky='w',columnspan=4)



# scrollframe

scroll_frame_saida = CTkScrollableFrame(master=frame_saida , border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78')
scroll_frame_saida.grid(row= 2, column= 0, rowspan= 4, padx=10)


# entry
entry_buscar_saida = CTkEntry(master=frame_saida,)
entry_buscar_saida.grid(row= 1, column = 0, padx = 10)

entry_NomeProd_saida = CTkEntry(master=frame_saida, state= 'disabled' )
entry_NomeProd_saida.grid(row = 1, column = 1, sticky = 'w',)

entry_qntdProd_saida = CTkEntry(master=frame_saida, width=70,  state= 'disabled' )
entry_qntdProd_saida.grid(row = 1, column = 1, padx=80)

entry_qntd_tirar_saida = CTkEntry(master=frame_saida, placeholder_text='Qtnd para tirar', width=120)
entry_qntd_tirar_saida.grid(row = 2, column = 1, sticky = 'w')





# checkbox

# -------------temporario--------------
for item in nomes:
   box = CTkCheckBox(master=scroll_frame_saida, text=item, corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6', )
   box.pack(pady=5, padx=10, fill="x")

# ------------------------------------
itens_saida2 = ["Item 1", "Item 2", "Item 3"]

scroll_frame_saida_prod = CTkScrollableFrame(master= frame_saida, border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78' )
scroll_frame_saida_prod.grid(row= 3, column= 1)

for item in enumerate (itens_saida2):  
    botao_remover_sair = CTkButton(master=scroll_frame_saida_prod, text="", image=image1, width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6')
    botao_remover_sair.grid(row=1, column=1, pady=2, padx=70, sticky='w')

    label_item_sair =CTkLabel(master=scroll_frame_saida_prod, text=item , width=50, fg_color="#8684EB")
    label_item_sair.grid(row=1, column=0, pady=2, padx=5)

# butao

btn_adicionarItem_saida = CTkButton(master= frame_saida, text='Adicionar Item', width=90, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6')
btn_adicionarItem_saida.grid(row = 2, column= 1, sticky='e',) 

btn_salvar_sair = CTkButton(master=frame_saida, text='salvar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6')
btn_salvar_sair.grid(row = 5, column= 1, sticky='e')

btn_salvar_cancelar = CTkButton(master=frame_saida, text='cancelar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6')
btn_salvar_cancelar.grid(row = 5, column= 1, sticky='w')
# frame entrada

# label
label_Entrada = CTkLabel(master=frame_entrada, text='Entrada', font=('Arial', 30),)
label_Entrada.grid(row = 0, column = 1, pady=30)


# frame relatorio

# label
label_Relatorio = CTkLabel(master=frame_relatorio, text='Relatorio', font=('Arial', 30),)
label_Relatorio.grid(row = 0, column = 1, pady=30)


root.mainloop()