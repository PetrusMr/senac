from customtkinter import *



def switch_event():
    
    if switch.get():
          
        frame_lateral.configure(border_color='#a399f9')   
        frame1.configure(border_color='#a399f9')
    else: 
        frame_lateral.configure(border_color='#d9d4fd')
        frame1.configure(border_color='#d9d4fd')

root = CTk()
root.geometry('820x400')
root.title('Sistema de gerenciamento')

# frame
frame_lateral = CTkFrame(master=root, width=190, height=390,  border_width=2)
frame_lateral.pack_propagate(False)
frame_lateral.grid(row = 0, column = 0, padx=10)

frame1 = CTkFrame(master=root, width= 590, height=390, border_width=2)
frame1.grid_propagate(False)
frame1.grid(row = 0, column = 1, padx = 5)

# frame_lateral widget

#label 
label_nome_sistema = CTkLabel(master=frame_lateral, text='Nome do\n Sistema', font=('Arial', 30))
label_nome_sistema.pack(pady = 30)

#butao
btn_cadastrar = CTkButton(master=frame_lateral, text='Cadastrar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_cadastrar.pack()

btn_editar = CTkButton(master= frame_lateral, text='Editar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_editar.pack(pady = 10)

btn_saida = CTkButton(master=frame_lateral, text='Saida', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_saida.pack()

btn_entrada = CTkButton(master=frame_lateral, text='Entrada', corner_radius=32, text_color='black', hover_color='#6e67a6')
btn_entrada.pack(pady=10)

btn_relatorio = CTkButton(master=frame_lateral, text='Relatorio', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_relatorio.pack()


switch = CTkSwitch(master=frame_lateral, text='SWITCH')
switch.pack()

# frame 01

# label
label_Cadrastro_produto = CTkLabel(master=frame1, text='Cadastro de Produto', font=('Arial', 30),)
label_Cadrastro_produto.grid(row = 0, column = 1, pady=30)


label_nome_produto = CTkLabel(master=frame1, text='Nome do Produto:', font=('Arial', 15),  )
label_nome_produto.grid(row = 1, column = 0, pady = 10, padx=30, sticky = 'e')

label_preco_produto = CTkLabel(master=frame1, text='Preço (R$):', font=('Arial', 15))
label_preco_produto.grid(row = 2, column = 0, pady = 10, padx=30,sticky = 'e')  

label_descricao = CTkLabel(master=frame1, text='Descrição:', font=('Arial', 15), )
label_descricao.grid(row = 3, column = 0, pady = 10, padx=30, sticky='ne')

# entry
entry_nome_produto = CTkEntry(master=frame1, width=300, placeholder_text='Nome do Produto', corner_radius=32,border_color='#a399f9')
entry_nome_produto.grid(row = 1, column = 1, pady = 10, sticky='w')

entry_preco = CTkEntry(master=frame1, width=80, placeholder_text='R$:', corner_radius=32, border_color='#a399f9')
entry_preco.grid(row=2, column=1, sticky='w')

# textbox

descricao_box = CTkTextbox(master=frame1, width=300, height=80,border_color='#a399f9', border_width=2, corner_radius=15)
descricao_box.grid(row=3, column=1, sticky='w',pady=12)

# butao

btn_salvar = CTkButton(master=frame1, width=80, text='Salvar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6')
btn_salvar.grid(row=4, column=1, pady=5,sticky='e')
root.mainloop()

