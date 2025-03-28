from PIL import Image
from customtkinter import *
from tkinter import ttk
import sqlite3
import os

produto_selecionado_id = None
produto_selecionado_id_saida = None
produto_selecionado_id_entrada = None


#import image
file_path = os.path.dirname(os.path.realpath(__file__))
#image1 = CTkImage(Image.open(fp= "C:/Users/970548/OneDrive - SENAC em Minas - EDU/Documentos/Senac/senac/UC5/projeto01/lixeira.png"), size=(25,25))
image = Image.open(file_path + "/lixeira.png")
image = image.resize((25,25))
image1 = CTkImage(image)

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


def fechar_banco():
    global banco
    if banco:
        banco.close()
   
   
checkboxes = {}

def preencher_campos_edit():
    global produto_selecionado_id
    
    for produto_id, checkbox in checkboxes.items():
        if checkbox.get() == 1:
            cursor.execute("SELECT nome, preco, descricao FROM produtos WHERE id = ?", (produto_id,))
            produto = cursor.fetchone()
            if produto:
                produto_selecionado_id = produto_id
                entry_nome_edit.delete(0, 'end')
                entry_nome_edit.insert(0, produto[0])  
                entry_preco_edit.delete(0, 'end')
                entry_preco_edit.insert(0, produto[1])  
                textbox_edit.delete('1.0', 'end')
                textbox_edit.insert('1.0', produto[2])  
            break  


def itens_laterais_edit():
       
    global banco, cursor  
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    cursor.execute("SELECT id, nome FROM produtos")
    produtos = cursor.fetchall()

    
    for widget in scroll_frame_edit.winfo_children():
        widget.destroy()

 



    def marcar_unico_edit(produto_id):
        for pid, checkbox in checkboxes.items():
            if pid != produto_id and checkbox.winfo_exists():  
                checkbox.deselect()
                entry_nome_edit.delete(0,'end')
                entry_preco_edit.delete(0,'end')
                textbox_edit.delete('1.0','end')
        preencher_campos_edit()
            
    for produto in produtos:
        produto_id, nome = produto
        var = IntVar()
        checkbox = CTkCheckBox(
            master=scroll_frame_edit,
            text=nome,
            variable=var,
            corner_radius=32,
            border_color='#a399f9',
            border_width=2,
            fg_color='#a399f9',
            text_color='white',
            hover_color='#6e67a6',
            command=lambda pid=produto_id: marcar_unico_edit(pid)
        )
        checkbox.pack(pady=5, padx=10, fill="x")
        checkboxes[produto_id] = checkbox

   
def switch_editar():
    frame_cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_editar.grid(row=0, column=1, padx=5)
    frame_editar.grid_propagate(False)

    itens_laterais_edit()

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='disabled')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='normal')


def filtro_edit(event):
    banco = sqlite3.connect("sistema_estoque.db")
    cursor = banco.cursor()

    def marcar_unico_edit(produto_id):
        
        for pid, checkbox in checkboxes.items():
            if pid != produto_id and checkbox.winfo_exists():
                checkbox.deselect() 
                entry_nome_edit.delete(0,'end')
                entry_preco_edit.delete(0,'end')
                textbox_edit.delete('1.0','end')
        preencher_campos_edit()
    

    for widget in scroll_frame_edit.winfo_children():
        widget.destroy()


    filtro = entry_busca_edit.get()
    cursor.execute('SELECT id, nome FROM produtos WHERE nome LIKE ?', (f'%{filtro}%',))

    filtrado = cursor.fetchall()


    if entry_busca_edit.get() == '':
        itens_laterais_edit()
        return
    else:
        

        for produto in filtrado:
            produto_id, nome = produto
            var = IntVar()
            checkbox = CTkCheckBox(
                master=scroll_frame_edit,
                text=nome,
                variable=var,
                corner_radius=32,
                border_color='#a399f9',
                border_width=2,
                fg_color='#a399f9',
                text_color='white',
                hover_color='#6e67a6',
                command=lambda pid=produto_id: marcar_unico_edit(pid))

            
                
            checkbox.pack(pady=5, padx=10, fill="x")
            checkboxes[produto_id] = checkbox
            preencher_campos_edit()

    banco.close()


def salvar_alteraçao_edit():
    global produto_selecionado_id
    nome = entry_nome_edit.get().strip()
    preco = entry_preco_edit.get().strip()
    descricao = textbox_edit.get('1.0', 'end').strip()


    sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()




    cursor.execute(
                "UPDATE produtos SET nome = ?, preco = ?, descricao = ? WHERE id = ?",
                (nome, preco, descricao, produto_selecionado_id)
            )
    banco.commit()
    banco.close()  

    entry_nome_edit.delete(0,'end')
    entry_preco_edit.delete(0,'end')
    textbox_edit.delete('1.0','end')  
    itens_laterais_edit()



def excluir_edit(): 
    global banco, cursor, checkboxes

    # Conecta ao banco de dados
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()

    # Itera sobre os checkboxes para encontrar os selecionados
    for produto_id, checkbox in checkboxes.items():
        if checkbox.get() == 1:  # Verifica se o checkbox está selecionado
            cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))

    # Confirma as alterações no banco de dados
    banco.commit()
    banco.close()

    # Limpa os campos de entrada e atualiza a lista de itens
    entry_nome_edit.delete(0, 'end')
    entry_preco_edit.delete(0, 'end')
    textbox_edit.delete('1.0', 'end')
    itens_laterais_edit()



def cancelar_editar():
    entry_preco_edit.delete(0,'end')
    entry_nome_edit.delete(0,'end')
    textbox_edit.delete('1.0','end')
    


linha = 0


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


def gerar_banco():
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos ( id integer primary key autoincrement, nome text not null , quantidade int not null ,preco decimal not null ,descricao text)""")
    banco.commit()
    banco.close()


def cadastrar_produto ():
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    cursor.execute("INSERT INTO produtos (nome, quantidade ,preco, descricao) VALUES (?,?,?,?)", (entry_nome_produto.get(), 0,entry_preco.get(), descricao_box.get('1.0', 'end')))
    banco.commit()
    banco.close()
    entry_nome_produto.delete(0, 'end')
    entry_preco.delete(0, 'end')
    descricao_box.delete('1.0', 'end')


def listar_produtos():
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM produtos")
    # produtos = cursor.fetchall()
    # banco.close()
    # return produtos


def carregar_estoque():
    # Conecta ao banco de dados
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    
    # Limpa o Treeview antes de i
    
    # Consulta os dados da tabela 'produtos'
    cursor.execute("SELECT nome, quantidade, preco, descricao FROM produtos")
    produtos = cursor.fetchall()
    
    # Insere os dados no Treeview
    for produto in produtos:
        estoque_tree.insert('', 'end', values=produto,)
    
    # Fecha a conexão com o banco
    banco.close()


def carregar_saida():
    # Conecta ao banco de dados
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    
    # Limpa o Treeview antes de i
    
    # Consulta os dados da tabela 'produtos'
    cursor.execute("SELECT nome, quantidade, preco, descricao FROM produtos")
    produtos = cursor.fetchall()
    
    # Insere os dados no Treeview
    for produto in produtos:
        estoque_tree.insert('', 'end', values=produto,)
    
    # Fecha a conexão com o banco
    banco.close()


def switch_relatorio():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_saida.grid_forget()
    frame_entrada.grid_forget()   
    frame_relatorio.grid(row=0, column=1, padx=5)
    frame_relatorio.grid_propagate(False)
    label_Relatorio.configure(text='Relatorio estoque')
    btn_estoque_relatorio.configure(state='disabled')
    btn_saida_relatorio.configure(state='normal')
    btn_entrada_relatorio.configure(state='normal')
    estoque_tree.grid(row=2, column=0, columnspan=4)
    saida_tree.grid_forget()
    entrada_tree.grid_forget()
    
    estoque_tree.delete(*estoque_tree.get_children())   

    carregar_estoque()

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='disabled')


def preencher_campos_saida():
    global produto_selecionado_id_saida, banco, cursor


    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()

    for produto_id, checkbox in checkboxes.items():
  
        if checkbox.get() == 1:
            cursor.execute("SELECT nome, quantidade FROM produtos WHERE id = ?", (produto_id,))
            produto = cursor.fetchone()

            if produto:
                produto_selecionado_id_saida = produto_id


                entry_nome_prod_saida.configure(state='normal')
                entry_qntd_tirar_saida.configure(state='normal')

                entry_nome_prod_saida.delete(0, 'end')
                entry_nome_prod_saida.insert(0, f"{produto[0]} ")
                entry_qntd_prod_saida.delete(0, 'end')
                entry_qntd_prod_saida.insert(0, f"{produto[1]}")
                entry_nome_prod_saida.configure(state='disabled')
                entry_qntd_prod_saida.configure(state='disabled')


            break


    banco.close()


def itens_laterais_saida():
       
    global banco, cursor  
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    cursor.execute("SELECT id, nome FROM produtos")
    produtos = cursor.fetchall()

    
    for widget in scroll_frame_saida.winfo_children():
        widget.destroy()

 




    def marcar_unico_saida(produto_id):
        
        for pid, checkbox in checkboxes.items():
            if pid != produto_id:
                checkbox.deselect()
                entry_qntd_prod_saida.configure(state='normal')
                entry_nome_prod_saida.configure(state='normal')
                entry_qntd_prod_saida.delete(0,'end')
                entry_nome_prod_saida.delete(0,'end')

                entry_nome_prod_saida.configure(state='disabled')
                

        preencher_campos_saida()

        
    for produto in produtos:
        produto_id, nome = produto
        var = IntVar()
        checkbox = CTkCheckBox(
            master=scroll_frame_saida,
            text=nome,
            variable=var,
            corner_radius=32,
            border_color='#a399f9',
            border_width=2,
            fg_color='#a399f9',
            text_color='white',
            hover_color='#6e67a6',
            command=lambda pid=produto_id: marcar_unico_saida(pid)
        )
        checkbox.pack(pady=5, padx=10, fill="x")
        checkboxes[produto_id] = checkbox


def switch_saida():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_saida.grid(row = 0, column = 1, padx = 5)
    frame_saida.grid_propagate(False)

    itens_laterais_saida()

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='disabled')
    btn_entrada.configure(state='normal')
    btn_relatorio.configure(state='normal')


def filtro_saida(event):
    banco = sqlite3.connect("sistema_estoque.db")
    cursor = banco.cursor()

    def marcar_unico_saida(produto_id):
        
        for pid, checkbox in checkboxes.items():
            if pid != produto_id and checkbox.winfo_exists():
                checkbox.deselect() 
        preencher_campos_saida()
    

    for widget in scroll_frame_saida.winfo_children():
        widget.destroy()


    filtro = entry_buscar_saida.get()
    cursor.execute('SELECT id, nome FROM produtos WHERE nome LIKE ?', (f'%{filtro}%',))

    filtrado = cursor.fetchall()


    if entry_buscar_saida.get() == '':
        itens_laterais_saida()
        return
    else:
        

        for produto in filtrado:
            produto_id, nome = produto
            var = IntVar()
            checkbox = CTkCheckBox(
                master=scroll_frame_saida,
                text=nome,
                variable=var,
                corner_radius=32,
                border_color='#a399f9',
                border_width=2,
                fg_color='#a399f9',
                text_color='white',
                hover_color='#6e67a6',
                command=lambda pid=produto_id: marcar_unico_saida(pid))

            
                
            checkbox.pack(pady=5, padx=10, fill="x")
            checkboxes[produto_id] = checkbox
            preencher_campos_saida()

    banco.close()



def delete_itens(label, button, item):

    if item in item_saida:
        index = item_saida.index(item)
        

        del item_saida[index]
        del quantidade_saida[index]
    

    label.grid_forget()
    button.grid_forget()



item_saida = []
quantidade_saida  = []

def adicionar_item_saida_func():
    global linha, quantidade_saida, item_saida

    entry_nome_prod_saida.configure(state='normal')

    item = entry_nome_prod_saida.get().split()

    linha += 1

    if item not in item_saida:
        item_saida.append(item)
        quantidade_saida.append(entry_qntd_tirar_saida.get())

        try:
            label = CTkLabel(scroll_frame_saida_prod, text=item, anchor="w")
            label.grid(row=linha, column=0, pady=5, padx=5)

            lixeira = CTkButton(
                scroll_frame_saida_prod, width=25, height=25, text="", 
                image=image1, fg_color='#a399f9', hover_color='#6e67a6', 
                command=lambda: delete_itens(label, lixeira, item)
            )
            lixeira.grid(row=linha, column=1, pady=5, padx=100, sticky='e')
            print(item_saida)
            print(quantidade_saida)



        except ValueError:
            return

    # entry_nome_prod_saida.configure(state='normal')
    # entry_qntd_prod_saida.configure (state='normal')

    # entry_nome_prod_saida.delete(0, 'end')
    # entry_qntd_tirar_saida.delete(0, 'end')
    # entry_qntd_prod_saida.delete(0, 'end')
    
    # entry_nome_prod_saida.configure(state='disabled')
    # entry_qntd_prod_saida.configure(state='disabled')

def salvar_alteracao_saida():
    global item_saida, quantidade_saida
    
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    
    for index, item in enumerate(item_saida):
        item = str(item[0])
        quantidade_atual = int(entry_qntd_prod_saida.get())

        quantidade = int(quantidade_saida[index])
        if quantidade > quantidade_atual or quantidade == 0:
            return
        else:
            quantidade = quantidade_atual - quantidade
        
            cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (quantidade, item))
    
    banco.commit()
    banco.close()
    item_saida.clear()
    quantidade_saida.clear()

def cancelar_saida():
    for widget in scroll_frame_saida_prod.winfo_children():
        widget.destroy()

    item_saida.clear()
    quantidade_saida.clear()

item_entrada = []
quantidade_entrada  = []

linha_entrada = 0


def preencher_campos_entrada():
    global produto_selecionado_id_saida, banco, cursor


    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()

    for produto_id, checkbox in checkboxes.items():
  
        if checkbox.get() == 1:
            cursor.execute("SELECT nome, quantidade FROM produtos WHERE id = ?", (produto_id,))
            produto = cursor.fetchone()

            if produto:
                produto_selecionado_id_saida = produto_id


                entry_nomeprod_entrada.configure(state='normal')
                entry_qntd_tirar_entrada.configure(state='normal')

                entry_nomeprod_entrada.delete(0, 'end')
                entry_nomeprod_entrada.insert(0, f"{produto[0]} ")
                entry_qntd_prod_entrada.delete(0, 'end')
                entry_qntd_prod_entrada.insert(0, f"{produto[1]}")
                entry_nomeprod_entrada.configure(state='disabled')
                entry_qntd_prod_entrada.configure(state='disabled')


            break



def itens_laterais_entrada():
       
       
    global banco, cursor  
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    cursor.execute("SELECT id, nome FROM produtos")
    produtos = cursor.fetchall()

    
    for widget in scroll_frame_entrada.winfo_children():
        widget.destroy()

 




    def marcar_unico_entrada(produto_id):
        
        for pid, checkbox in checkboxes.items():
            if pid != produto_id:
                checkbox.deselect()
                entry_qntd_prod_entrada.configure(state='normal')
                entry_qntd_prod_entrada.delete(0,'end')
                
        preencher_campos_entrada()

        
    for produto in produtos:
        produto_id, nome = produto
        var = IntVar()
        checkbox = CTkCheckBox(
            master=scroll_frame_entrada,
            text=nome,
            variable=var,
            corner_radius=32,
            border_color='#a399f9',
            border_width=2,
            fg_color='#a399f9',
            text_color='white',
            hover_color='#6e67a6',
            command=lambda pid=produto_id: marcar_unico_entrada(pid)
        )
        checkbox.pack(pady=5, padx=10, fill="x")
        checkboxes[produto_id] = checkbox

def delete_itens_entrada(label, button, item):

    if item in item_saida:
        index = item_saida.index(item)
        

        del item_saida[index]
        del quantidade_saida[index]
    

    label.grid_forget()
    button.grid_forget()



def adicionar_item_entrada_func():
    global linha_entrada, quantidade_entrada, item_entrada

    entry_nomeprod_entrada.configure(state='normal')

    item = entry_nomeprod_entrada.get().split()

    linha_entrada += 1

    if item not in item_entrada:
        item_entrada.append(item)
        quantidade_entrada.append(entry_qntd_tirar_entrada.get())

        try:
            label = CTkLabel(scroll_frame_entrada_prod, text=item, anchor="w")
            label.grid(row=linha_entrada, column=0, pady=5, padx=5)

            lixeira = CTkButton(
                scroll_frame_entrada_prod, width=25, height=25, text="", 
                image=image1, fg_color='#a399f9', hover_color='#6e67a6', 
                command=lambda: delete_itens_entrada(label, lixeira, item)
            )
            lixeira.grid(row=linha_entrada, column=1, pady=5, padx=100, sticky='e')
            print(item_entrada)
            print(quantidade_entrada)



        except ValueError:
            return
        
    entry_qntd_prod_entrada.configure(state='normal')
    
    
    # entry_qntd_prod_entrada.delete(0, 'end')
    # entry_nomeprod_entrada.delete(0, 'end')
    # entry_qntd_tirar_entrada.delete(0, 'end')
    
    # entry_qntd_prod_entrada.configure(state='disabled')
    # entry_nomeprod_entrada.configure(state='disabled')
    

def switch_entrada():
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()    
    frame_saida.grid_forget()
    frame_relatorio.grid_forget()
    frame_entrada.grid(row = 0, column = 1, padx = 5)
    frame_entrada.grid_propagate(False)

    itens_laterais_entrada()

    btn_cadastrar.configure(state='normal')
    btn_editar.configure(state='normal')
    btn_saida.configure(state='normal')
    btn_entrada.configure(state='disabled')
    btn_relatorio.configure(state='normal')


def filtro_entrada(event):
    banco = sqlite3.connect("sistema_estoque.db")
    cursor = banco.cursor()

    def marcar_unico_entrada(produto_id):
        
        for pid, checkbox in checkboxes.items():
            if pid != produto_id and checkbox.winfo_exists():
                checkbox.deselect() 
        preencher_campos_entrada()
    

    for widget in scroll_frame_entrada.winfo_children():
        widget.destroy()


    filtro = entry_buscar_entrada.get()
    cursor.execute('SELECT id, nome FROM produtos WHERE nome LIKE ?', (f'%{filtro}%',))

    filtrado = cursor.fetchall()


    if entry_buscar_entrada.get() == '':
        itens_laterais_entrada()
        return
    else:
        

        for produto in filtrado:
            produto_id, nome = produto
            var = IntVar()
            checkbox = CTkCheckBox(
                master=scroll_frame_entrada,
                text=nome,
                variable=var,
                corner_radius=32,
                border_color='#a399f9',
                border_width=2,
                fg_color='#a399f9',
                text_color='white',
                hover_color='#6e67a6',
                command=lambda pid=produto_id: marcar_unico_entrada(pid))

            
                
            checkbox.pack(pady=5, padx=10, fill="x")
            checkboxes[produto_id] = checkbox
            preencher_campos_entrada()

    banco.close()

def salvar_alteracao_entrada():
    global item_entrada, quantidade_entrada
    
    banco = sqlite3.connect('sistema_estoque.db')
    cursor = banco.cursor()
    
    for index, item in enumerate(item_entrada):
        item = str(item[0])
        quantidade_atual = int(entry_qntd_prod_entrada.get())

        quantidade = int(quantidade_entrada[index])

        quantidade = quantidade_atual + quantidade
        
        cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (quantidade, item))
    
    banco.commit()
    banco.close()
    item_entrada.clear()
    quantidade_entrada.clear()

def cancelar_entrada():
    for widget in scroll_frame_entrada_prod.winfo_children():
        widget.destroy()

    item_entrada.clear()
    quantidade_entrada.clear()



root = CTk()
root.geometry('840x400')
root.title('Sistema de gerenciamento')
# gerar_banco()

# style do tree view
style = ttk.Style(master=root)
style.theme_use('clam')
style.configure("Treeview", background="#a399f9", fieldbackground="#565b5e", foreground="black",rowheight=25,bordercolor="#343638", )

style.configure("Treeview.Heading",background="#565b5e",foreground="black",relief="flat")
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

btn_salvar = CTkButton(master=frame_cadastrar, width=80, text='Salvar', corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command=cadastrar_produto)
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
entry_busca_edit.bind("<KeyRelease>", filtro_edit)


entry_nome_edit = CTkEntry(master=frame_editar, placeholder_text='Nome do Produto', width=250, border_color='#a399f9', corner_radius=32)
entry_nome_edit.grid(row=2, column = 1,  sticky  = 'w', pady=5 )

entry_preco_edit = CTkEntry(master=frame_editar, placeholder_text='R$:', width=80, border_color='#a399f9', corner_radius=32)
entry_preco_edit.grid(row=3, column = 1, sticky  = 'nw',)

# textbox
textbox_edit = CTkTextbox(master=frame_editar,height=150, width=280, border_color='#a399f9', border_width=2, corner_radius=15, scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#6e67a6')
textbox_edit.grid(row=4, column = 1, sticky ='w', pady=5,)


# butao 

btn_salvar_edit = CTkButton(master=frame_editar, text= 'Salvar', width=90, corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6' ,command=salvar_alteraçao_edit)
btn_salvar_edit.grid(row=5, column=1,pady=5, sticky='e')

btn_excluir_edit = CTkButton(master=frame_editar, text='Excluir', width=90, corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command=excluir_edit)
btn_excluir_edit.grid(row=5, column=1,pady=5, )

btn_cancelar_edit = CTkButton(master=frame_editar, text='Cancelar',width=90, corner_radius=32, fg_color='#a399f9', text_color='black', hover_color='#6e67a6', command= cancelar_editar)
btn_cancelar_edit.grid(row=5, column=1,pady=5, sticky='w')


# frame saida

# Label
label_saida = CTkLabel(master=frame_saida, text='Saida de Produto', font=('Arial', 20),)
label_saida.grid(row = 0, column = 0, pady=5, padx= 200,sticky='w',columnspan=4)



# scrollframe

scroll_frame_saida = CTkScrollableFrame(master=frame_saida , border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78')
scroll_frame_saida.grid(row= 2, column= 0, rowspan= 4, padx=10)


# entry
entry_buscar_saida = CTkEntry(master=frame_saida, width=219, placeholder_text="Buscar Produto", border_color='#a399f9', corner_radius=32)
entry_buscar_saida.grid(row= 1, column = 0, padx = 30, sticky='w')
entry_buscar_saida.bind("<KeyRelease>", filtro_saida)

entry_nome_prod_saida = CTkEntry(master=frame_saida, border_color='#a399f9', corner_radius=32 )
entry_nome_prod_saida.grid(row = 1, column = 1, sticky = 'w', padx = 5)

entry_qntd_prod_saida = CTkEntry(master=frame_saida, border_color='#a399f9', corner_radius=32, width=80,)
entry_qntd_prod_saida.grid(row = 1, column = 1, sticky = 'e', padx = 5)


entry_qntd_tirar_saida = CTkEntry(master=frame_saida, placeholder_text='Qtnd para -', width=120, border_color='#a399f9', corner_radius=32)
entry_qntd_tirar_saida.grid(row = 2, column = 1, sticky = 'w', padx=5)




scroll_frame_saida_prod = CTkScrollableFrame(master= frame_saida, border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78',)
scroll_frame_saida_prod.grid(row= 3, column= 1)


# butao

btn_adicionar_item_saida = CTkButton(master= frame_saida, text='Adicionar Item', width=90, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black',command=adicionar_item_saida_func)
btn_adicionar_item_saida.grid(row = 2, column= 1, sticky='e',pady=5) 

btn_salvar_sair = CTkButton(master=frame_saida, text='salvar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6',text_color='black', command=salvar_alteracao_saida)
btn_salvar_sair.grid(row = 5, column= 1, sticky='e')

btn_salvar_cancelar_saida = CTkButton(master=frame_saida, text='cancelar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=cancelar_saida)
btn_salvar_cancelar_saida.grid(row = 5, column= 1, sticky='w', pady=5)


# frame entrada

# label
label_Entrada = CTkLabel(master=frame_entrada, text='Entrada', font=('Arial', 20),)
label_Entrada.grid(row = 0, column = 0, pady=5, padx= 237,sticky='w',columnspan=4)

# scrollframe

scroll_frame_entrada = CTkScrollableFrame(master=frame_entrada , border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78')
scroll_frame_entrada.grid(row= 2, column= 0, rowspan= 4, padx=10)


# entry
entry_buscar_entrada = CTkEntry(master=frame_entrada,width=219, placeholder_text="Buscar Produto" ,border_color='#a399f9', corner_radius=32)
entry_buscar_entrada.grid(row= 1, column = 0, padx = 20, sticky = 'w')
entry_buscar_entrada.bind("<KeyRelease>", filtro_entrada)

entry_nomeprod_entrada = CTkEntry(master=frame_entrada, state= 'disabled', border_color='#a399f9', corner_radius=32 )
entry_nomeprod_entrada.grid(row = 1, column = 1, sticky = 'w', padx=5)

entry_qntd_prod_entrada = CTkEntry(master=frame_entrada, border_color='#a399f9', corner_radius=32, width=80,)
entry_qntd_prod_entrada.grid(row = 1, column = 1, sticky = 'e', padx = 5)

entry_qntd_tirar_entrada = CTkEntry(master=frame_entrada, placeholder_text='Qtnd para +', width=120, border_color='#a399f9', corner_radius=32)
entry_qntd_tirar_entrada.grid(row = 2, column = 1, sticky = 'w', padx= 5)



scroll_frame_entrada_prod = CTkScrollableFrame(master= frame_entrada, border_color='#a399f9', border_width=2,scrollbar_fg_color='#6e67a6', scrollbar_button_color='#a399f9', scrollbar_button_hover_color='#544a78' )
scroll_frame_entrada_prod.grid(row= 3, column= 1)



# butao

btn_adicionarItem_entrada = CTkButton(master= frame_entrada, text='Adicionar Item', width=90, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=adicionar_item_entrada_func)
btn_adicionarItem_entrada.grid(row = 2, column= 1, sticky='e',pady=5,) 

btn_salvar_entrada = CTkButton(master=frame_entrada, text='salvar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6', text_color='black', command=salvar_alteracao_entrada)
btn_salvar_entrada.grid(row = 5, column= 1, sticky='e')

btn_salvar_cancelar_entrada = CTkButton(master=frame_entrada, text='cancelar',width=50, fg_color="#8684EB", corner_radius=32, hover_color='#6e67a6',text_color='black', command=cancelar_entrada) 
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
estoque_tree.column('quantidade',width=110 , anchor=CENTER )
estoque_tree.column('preço',width=110 , anchor=CENTER )
estoque_tree.column('descricao',width=110 )


# treeview saida
columns_saida = ('nome', 'quantidade', 'Data/hora')

saida_tree = ttk.Treeview(master=frame_relatorio, columns=columns_saida, show='headings', )

saida_tree.heading('nome', text='nome')
saida_tree.heading('quantidade', text='quantidade')
saida_tree.heading('Data/hora', text='Data/hora')


saida_tree.column('nome',width=110 )
saida_tree.column('quantidade',width=110  , anchor=CENTER)
saida_tree.column('Data/hora',width=110  , anchor=CENTER)


# treeview entrada
columns_entrada = ('nome', 'quantidade', 'Data/hora')

entrada_tree = ttk.Treeview(master=frame_relatorio, columns=columns_entrada, show='headings', )

entrada_tree.heading('nome', text='nome')
entrada_tree.heading('quantidade', text='quantidade')
entrada_tree.heading('Data/hora', text='Data/hora')

entrada_tree.heading('Data/hora', text='Data/hora')



entrada_tree.column('nome',width=110  )
entrada_tree.column('quantidade',width=110  , anchor=CENTER)
entrada_tree.column('Data/hora',width=110  , anchor=CENTER)

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