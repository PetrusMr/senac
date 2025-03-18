from customtkinter import *
import sqlite3


def criar_DB ():
    banco = sqlite3.connect("Banco_Dados.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nomes (nome text)")
    banco.commit()
    banco.close()

def cadastro():
    banco = sqlite3.connect("Banco_Dados.db")
    cursor = banco.cursor()
    nome = entry_teste.get()
    cursor.execute('insert into nomes values("'+nome+'")')
    banco.commit()
    banco.close()

def saida():
    banco = sqlite3.connect("Banco_Dados.db")
    cursor = banco.cursor() 
    cursor.execute('select * from nomes')
    lb_saida.configure(text=cursor.fetchall())  


root = CTk()
root.geometry("300x300")
criar_DB()

lb_titulo = CTkLabel(master=root, text='Sistema Salvar Nome')
lb_titulo.pack(pady=12)


entry_teste = CTkEntry(master=root)
entry_teste.pack(pady=10)

btn_cadastrar = CTkButton(master=root, text='Cadastrar', command=cadastro)
btn_cadastrar.pack(pady=12)

btn_visualizar = CTkButton(master=root, text="Visualizar", command=saida )
btn_visualizar.pack()

lb_saida = CTkLabel(master=root, text='')
lb_saida.pack(pady=12)

root.mainloop()