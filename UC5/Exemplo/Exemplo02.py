from customtkinter import *
#aa
def soma():
    nm1 = float(entry_1.get())
    nm2 = float(entry_2.get())
    sam = nm1 + nm2

    lab_resultado.configure(text =sam )



set_appearance_mode('Dark')
root = CTk()

root.geometry('400x300')
root.title('Soma de 2 numeros')
root.resizable(FALSE,False)

frame = CTkFrame(master=root, width=500, height=600, border_color='#8c16e7', border_width=2)
frame.pack(pady = 24)

lab_Titulo = CTkLabel(master=frame, text='Soma')
lab_Titulo.pack(pady=12)

entry_1 = CTkEntry(master=frame, placeholder_text='Primeiro numero',  border_color='#8c16e7', border_width=2)
entry_1.pack()

entry_2 = CTkEntry(master=frame, placeholder_text='Segundo numero',  border_color='#8c16e7', border_width=2)
entry_2.pack(pady=20)

btn = CTkButton(master= frame, text='Somar', command=soma, fg_color='#8c16e7' )
btn.pack()

lab_resultado = CTkLabel(master=frame, text='')
lab_resultado.pack(pady=12)


root.mainloop()