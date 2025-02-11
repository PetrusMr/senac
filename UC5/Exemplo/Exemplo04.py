from customtkinter import *

salto = []
nome = ""

def salvar():
    global nome, salto
    nome = entry_nome.get()
    temp = float(entry_salto.get())
    salto.append(temp)
    entry_salto.delete(0, END)
    



def confirmar():
    global nome, salto
    media_salto = sum(salto)/ len(salto)
    set_appearance_mode('Dark')
    root1 = CTkToplevel( root)
    root1.title('Resultado')
    root1.geometry('500x400')
    root1.resizable(FALSE, False)
    root1.attributes("-topmost", True)


    label_text = CTkLabel(master=root1, text='Resultado' ,font=('Arial',20))
    label_text.place(relx = 0.4, rely  = 0.2, )
    


    label_nome = CTkLabel(master = root1, text=f'Nome: {nome}', font=('Arial',15))
    label_nome.place(relx = 0.3, rely  = 0.3, )
    
    label_saltos = CTkLabel(master=root1, text=f'Os saltos: {salto}', font=('Arial',15))    
    label_saltos.place(relx = 0.3, rely  = 0.4, )

    label_media = CTkLabel(master=root1, text=f'Media de salto: {media_salto}', font=('Arial',15))
    label_media.place(relx = 0.3, rely  = 0.5, )
 
    salto.clear()
    root1.mainloop()


set_appearance_mode('Dark')

root = CTk()
root.title('Info')

root.geometry('500x400')
root.resizable(FALSE, False)


lb_titulo = CTkLabel(master=root, text='Calculo de Salto', font=('Arial',20))
lb_titulo.place(relx = 0.39, rely  = 0.1, )

lb_nome = CTkLabel(master=root, text='Nome: ', font=('Arial',15))
lb_nome.place(relx = 0.3, rely  = 0.3, )

entry_nome = CTkEntry(master=root, border_color='#f72491', border_width=2, placeholder_text='Nome:')
entry_nome.place(relx = 0.4, rely = 0.3)



lb_salto = CTkLabel(master=root, text='Salto: ', font=('Arial',15))
lb_salto.place(relx = 0.3, rely  = 0.4, )

entry_salto = CTkEntry(master=root, border_color='#f72491', border_width=2, placeholder_text='Informe em metros:')
entry_salto.place(relx = 0.4, rely = 0.4)

btn_salvar = CTkButton(master=root, text='Salvar',command=salvar, fg_color='#f72491', hover_color='#a1195f')
btn_salvar.place(relx=0.4 , rely = 0.5)

btn_r = CTkButton(master=root, text='Resultado', command=confirmar, fg_color='#f72491', hover_color='#a1195f')
btn_r.place(relx=0.4 , rely = 0.6)



root.mainloop()