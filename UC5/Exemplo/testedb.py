from customtkinter import *
import sqlite3


def criar_DB ():
    banco = sqlite3.connect("Banco_Dados.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS nomes (nome text, id int)")
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

lb_titulo = CTkLabel(master=root, text='Sistema Salvar Nome').pack(pady=12)


entry_teste = CTkEntry(master=lb_titulo).pack(pady=10)

btn_cadastrar = CTkButton(master=root, text='Cadastrar', command=cadastro).pack(pady=12)

btn_visualizar = CTkButton(master=root, text="Visualizar", command=saida ).pack()

lb_saida = CTkLabel(master=root, text='').pack(pady=12)

root.mainloop()