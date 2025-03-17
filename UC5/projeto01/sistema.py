from PIL import Image
from customtkinter import *
from tkinter import ttk
import sqlite3
import os





#import image
file_path = os.path.dirname(os.path.realpath(__file__))
image1 = CTkImage(Image.open(fp= "C:/Users/970548/OneDrive - SENAC em Minas - EDU/Documentos/Senac/senac/UC5/projeto01/lixeira.png"), size=(25,25))

# thema_ctk
set_appearance_mode("dark")

#função
def switch_cadastrar():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_cadastrar.grid(row = 0, column = 1, padx = 5)
    frame_cadastrar.grid_propagate(False)

    btn_cadastrar.configure(state='disabled')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='normal')


def switch_editar():
    frame_cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_editar.grid(row = 0, column = 1, padx = 5)
    frame_editar.grid_propagate(False)

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='disabled')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='normal')
 

def switch_saida():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida.grid(row = 0, column = 1, padx = 5)
    frame_saida.grid_propagate(False)

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='disabled')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='normal')


def switch_entrada():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_saida.grid_forget()
    frame_relatorio.grid_forget()
    frame_entrada.grid(row = 0, column = 1, padx = 5)
    frame_entrada.grid_propagate(False)

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='disabled')
    btn_relatorio.configure(state='normal')


def switch_relatorio():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_saida.grid_forget()
    frame_entrada.grid_forget()    
    frame_relatorio.grid(row = 0, column = 1, padx = 5)
    frame_relatorio.grid_propagate(False)
    label_Relatorio.configure(text='Relatorio estoque')
    btn_estoque_relatorio.configure(state='disabled')
    btn_saida_relatorio.configure(state='normal')
    btn_entrada_relatorio.configure(state='normal')
    estoque_tree.grid(row=2, column=0, columnspan=4)
    saida_tree.grid_forget()
    entrada_tree.grid_forget()

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='disabled')


def delete_itens(linhas, botoes):
    linhas.grid_forget()
    botoes.grid_forget()
 
linha = 0

def adicionar_item_saida():  
    global linha
    item_vet = str(entry_qntd_tirar_saida.get())
    linha += 1
 
    if item_vet in nomes:    
        try :  
            label = CTkLabel(scroll_frame_saida_prod, text=item_vet, anchor="w")            
            label.grid(row=linha, column=0, pady=5, padx=5, sticky='w')    
            lixeira = CTkButton(scroll_frame_saida_prod, width=25, height=25, text="", image=image1, fg_color='#a399f9', hover_color='#6e67a6' ,command=lambda: delete_itens(label, lixeira),)
            lixeira.grid(row=linha, column=1, pady=5, padx=100, sticky='e')
 
        except ValueError:
            return  
        

def adicionar_item_entrada():  
    global linha
    item_vet = str(entry_qntd_tirar_entrada.get())
    linha += 1
 
    if item_vet in nomes:    
        try :  
            label_entrada_prod = CTkLabel(scroll_frame_entrada_prod, text=item_vet, anchor="w")            
            label_entrada_prod.grid(row=linha, column=0, pady=5, padx=5, sticky = 'w')    
            lixeira = CTkButton(scroll_frame_entrada_prod, width=25, height=25, text="", image=image1, fg_color='#a399f9', hover_color='#6e67a6' ,command=lambda: delete_itens(label_entrada_prod, lixeira),)
            lixeira.grid(row=linha, column=1, pady=5, padx=100, sticky='e')
 
        except ValueError:
            return
        

def export():
    root_export = CTkToplevel()
    root_export.geometry('570x330')
    root_export.title('')
    root_export.attributes('-topmost',True)

    # frame
    frame_root_exportar = CTkFrame(master=root_export, width=500, height=300,border_color='#d9d4fd', border_width=2)
    frame_root_exportar.pack(anchor='center')
    frame_root_exportar.grid_propagate(False)


    # label
    escolher_relatorio = CTkLabel(master=frame_root_exportar, text='Escolher Relatorio(s)', font=('Arial', 20))
    escolher_relatorio.grid(row=0, column=0, pady=30)

    Escolher_extensao = CTkLabel(master=frame_root_exportar, text='Escolher extensão',font=('Arial', 20))
    Escolher_extensao.grid(row=0, column=1, pady=10, padx=50)



    # checkbox
    exportar_estoque_root_exportar = CTkCheckBox(master=frame_root_exportar, text='Exportar estoque',font=('Arial', 15), corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6',).grid(row=1, column=0, sticky='w', padx=50)
    exportar_saida_root_exportar = CTkCheckBox(master=frame_root_exportar, text='Exportar saida',font=('Arial', 15), corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6',).grid(row=2, column=0, sticky='w',padx=50, pady=5)
    exportar_entrada_root_exportar = CTkCheckBox(master=frame_root_exportar, text='Exportar entrada',font=('Arial', 15), corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6',).grid(row=3, column=0, sticky='w', padx=50)
    word_exportar = CTkCheckBox(master=frame_root_exportar, text='WORD',font=('Arial', 15), corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6',).grid(row=1, column=1, sticky='w',padx='100')
    pdf_exportar = CTkCheckBox(master=frame_root_exportar, text='PDF',font=('Arial', 15), corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6',).grid(row=2, column=1, sticky='w',padx='100')
    excel_exportar = CTkCheckBox(master=frame_root_exportar, text='EXCEL',font=('Arial', 15), corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6',).grid(row=3, column=1, sticky='w',padx='100')
    
    
    # button
    btn_save_frame_exportar = CTkButton(master=frame_root_exportar, text='SALVAR', width=70, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black')
    btn_save_frame_exportar.grid(row=4, column=0, pady=20, sticky='e', columnspan=1)

    btn_cancel_frame_exportar = CTkButton(master=frame_root_exportar, text='CANCELAR', width=70, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black')
    btn_cancel_frame_exportar.grid(row=4, column=1,sticky='w',padx=20, )


def switch_saida_relatorio():
    estoque_tree.grid_forget()
    entrada_tree.grid_forget()
    saida_tree.grid(row=2, column=0, columnspan=4)
    label_Relatorio.configure(text='Saida estoque')
    btn_estoque_relatorio.configure(state='normal')
    btn_entrada_relatorio.configure(state='normal')
    btn_saida_relatorio.configure(state='disabled')


def switch_entrada_relatorio():
    estoque_tree.grid_forget()
    entrada_tree.grid(row=2, column=0, columnspan=4)
    saida_tree.grid_forget()
    label_Relatorio.configure(text='Entrada estoque')
    btn_estoque_relatorio.configure(state='normal')
    btn_entrada_relatorio.configure(state='disabled')
    btn_saida_relatorio.configure(state='normal')


root = CTk()
root.geometry('840x400')
root.title('Sistema de gerenciamento')

# style do tree view
style = ttk.Style(master=root)
style.theme_use('clam')
style.configure("Treeview", background="#3484F0", fieldbackground="#565b5e", foreground="white",rowheight=25,bordercolor="#343638", )

style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
style.map("Treeview.Heading",background=[('active', '#a399f9')])

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
label_nome_sistema = CTkLabel(master=frame_lateral, text='SGE', font=('Arial', 30))
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
   box_edit = CTkCheckBox(master=scroll_frame_edit, text=item, corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6', )
   box_edit.pack(pady=5, padx=10, fill="x")




# frame saida

# Label
label_saida = CTkLabel(master=frame_saida, text='Saida de Produto', font=('Arial', 20),)
label_saida.grid(row = 0, column = 0, pady=5, padx= 200,sticky='w',columnspan=4)



# scrollframe

scroll_frame_saida = CTkScrollableFrame(master=frame_saida , border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78')
scroll_frame_saida.grid(row= 2, column= 0, rowspan= 4, padx=10)


# entry
entry_buscar_saida = CTkEntry(master=frame_saida, width=219, border_color='#a399f9', corner_radius=32)
entry_buscar_saida.grid(row= 1, column = 0, padx = 30, sticky='w')

entry_nome_prod_saida = CTkEntry(master=frame_saida, state= 'disabled', border_color='#a399f9', corner_radius=32 )
entry_nome_prod_saida.grid(row = 1, column = 1, sticky = 'w', padx = 5)

entry_qntd_tirar_saida = CTkEntry(master=frame_saida, placeholder_text='Qtnd para -', width=120, border_color='#a399f9', corner_radius=32)
entry_qntd_tirar_saida.grid(row = 2, column = 1, sticky = 'w', padx=5)





# checkbox

# -------------temporario--------------
for item in nomes:
   box_saida = CTkCheckBox(master=scroll_frame_saida, text=item, corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6', )
   box_saida.pack(pady=5, padx=10, fill="x")

# ------------------------------------


scroll_frame_saida_prod = CTkScrollableFrame(master= frame_saida, border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78',)
scroll_frame_saida_prod.grid(row= 3, column= 1)



# butao

btn_adicionar_item_saida = CTkButton(master= frame_saida, text='Adicionar Item', width=90, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black',command=adicionar_item_saida)
btn_adicionar_item_saida.grid(row = 2, column= 1, sticky='e',pady=5) 

btn_salvar_sair = CTkButton(master=frame_saida, text='salvar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6',text_color='black')
btn_salvar_sair.grid(row = 5, column= 1, sticky='e')

btn_salvar_cancelar_saida = CTkButton(master=frame_saida, text='cancelar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black')
btn_salvar_cancelar_saida.grid(row = 5, column= 1, sticky='w', pady=5)


# frame entrada

# label
label_Entrada = CTkLabel(master=frame_entrada, text='Entrada', font=('Arial', 20),)
label_Entrada.grid(row = 0, column = 0, pady=5, padx= 237,sticky='w',columnspan=4)

# scrollframe

scroll_frame_entrada = CTkScrollableFrame(master=frame_entrada , border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78')
scroll_frame_entrada.grid(row= 2, column= 0, rowspan= 4, padx=10)


# entry
entry_buscar_entrada = CTkEntry(master=frame_entrada,width=219, border_color='#a399f9', corner_radius=32)
entry_buscar_entrada.grid(row= 1, column = 0, padx = 20, sticky = 'w')

entry_NomeProd_entrada = CTkEntry(master=frame_entrada, state= 'disabled', border_color='#a399f9', corner_radius=32 )
entry_NomeProd_entrada.grid(row = 1, column = 1, sticky = 'w', padx=5)

entry_qntd_tirar_entrada = CTkEntry(master=frame_entrada, placeholder_text='Qtnd para +', width=120, border_color='#a399f9', corner_radius=32)
entry_qntd_tirar_entrada.grid(row = 2, column = 1, sticky = 'w', padx= 5)



# checkbox

# -------------temporario--------------
for item in nomes:
   box_entrada = CTkCheckBox(master=scroll_frame_entrada, text=item, corner_radius=32, border_color='#a399f9', border_width=2, fg_color='#a399f9', text_color='white', hover_color='#6e67a6', )
   box_entrada.pack(pady=5, padx=10, fill="x")

# ------------------------------------

scroll_frame_entrada_prod = CTkScrollableFrame(master= frame_entrada, border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78' )
scroll_frame_entrada_prod.grid(row= 3, column= 1)



# butao

btn_adicionarItem_entrada = CTkButton(master= frame_entrada, text='Adicionar Item', width=90, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black',command=adicionar_item_entrada)
btn_adicionarItem_entrada.grid(row = 2, column= 1, sticky='e',pady=5,) 

btn_salvar_entrada = CTkButton(master=frame_entrada, text='salvar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black')
btn_salvar_entrada.grid(row = 5, column= 1, sticky='e')

btn_salvar_cancelar_entrada = CTkButton(master=frame_entrada, text='cancelar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6',text_color='black' )
btn_salvar_cancelar_entrada.grid(row = 5, column= 1, sticky='w', pady=5, padx=5)




# frame relatorio

# label
label_Relatorio = CTkLabel(master=frame_relatorio, text='Relatorio estoque', font=('Arial', 20),)
label_Relatorio.grid(row = 0, column = 0, pady=5,padx = 20 , sticky='e')

# entry
entry_busca_relatorio_estoque = CTkEntry(master=frame_relatorio, placeholder_text='Buscar Produto', width=200, border_color='#a399f9', corner_radius=32)
entry_busca_relatorio_estoque.grid(row=1, column = 0, padx=30, sticky  = 'w')


# treeview_estoque

columns_estoque = ('nome', 'quantidade', 'preço', 'descricao')

estoque_tree = ttk.Treeview(master=frame_relatorio, columns=columns_estoque, show='headings', )
estoque_tree.grid(row=2, column=0, columnspan=4)

estoque_tree.heading('nome', text='nome')
estoque_tree.heading('quantidade', text='quantidade')
estoque_tree.heading('preço', text='preço')
estoque_tree.heading('descricao', text='descricao')

estoque_tree.column('nome',width=110 )
estoque_tree.column('quantidade',width=110 )
estoque_tree.column('preço',width=110 )
estoque_tree.column('descricao',width=110 )


# treeview saida
columns_saida = ('nome', 'quantidade', 'Data/hora')

saida_tree = ttk.Treeview(master=frame_relatorio, columns=columns_saida, show='headings', )

saida_tree.heading('nome', text='nome')
saida_tree.heading('quantidade', text='quantidade')
saida_tree.heading('Data/hora', text='Data/hora')


saida_tree.column('nome',width=110 )
saida_tree.column('quantidade',width=110 )
saida_tree.column('Data/hora',width=110 )


# treeview entrada
columns_entrada = ('nome', 'quantidade', 'Data/hora')

entrada_tree = ttk.Treeview(master=frame_relatorio, columns=columns_entrada, show='headings', )

entrada_tree.heading('nome', text='nome')
entrada_tree.heading('quantidade', text='quantidade')
entrada_tree.heading('Data/hora', text='Data/hora')

entrada_tree.heading('Data/hora', text='Data/hora')



entrada_tree.column('nome',width=110 )
entrada_tree.column('quantidade',width=110 )
entrada_tree.column('Data/hora',width=110 )

# button
btn_exportar_relatorio = CTkButton(master=frame_relatorio, text='Exportar', width=70, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=export)
btn_exportar_relatorio.grid(row = 1, column= 2, sticky='w',pady=5, )

btn_estoque_relatorio = CTkButton(master=frame_relatorio, text='Estoque', width=70, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=switch_relatorio)
btn_estoque_relatorio.grid(row = 3, column= 1,pady=5,sticky='w' )

btn_entrada_relatorio = CTkButton(master=frame_relatorio, text='Entrada', width=70, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=switch_entrada_relatorio)
btn_entrada_relatorio.grid(row = 3, column= 1,pady=5, padx=80  )

btn_saida_relatorio = CTkButton(master=frame_relatorio, text='Saida', width=70, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=switch_saida_relatorio)
btn_saida_relatorio.grid(row = 3, column= 1,pady=5,sticky='e',  )





root.mainloop()