from customtkinter import *

def pegar_texto(): 
    texto = txt_entry.get()
    label_saida.configure(text= texto)

set_appearance_mode('Dark')
set_default_color_theme('blue')

root = CTk()

root.geometry('400x300')
root.title('Exemplo')

Label_ola = CTkLabel(master=root, text='Olá mundo !!', font=('Arial' , 35, 'bold'), text_color='white')
Label_ola.pack()

txt_entry = CTkEntry(master=root, border_color='#6e26a5', border_width=2, placeholder_text='Escreva', text_color='red', placeholder_text_color='green'  )
txt_entry.pack(pady=20)

btn = CTkButton(master=root, text= 'Clique aki', border_color='#6e26a5', border_width=2, fg_color='#6e26a5', hover_color='black', command=pegar_texto)
btn.pack()

label_saida = CTkLabel(master= root, text='' )
label_saida.pack(pady=12)

root.mainloop()