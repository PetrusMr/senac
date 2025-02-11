from customtkinter import *


root = CTk()
root.geometry('600x300')

frame01 = CTkFrame(master=root, width=300, height=300, corner_radius= 0, fg_color='#7a47ce' )
frame01.grid(row = 0, column = 0)

frame02 = CTkFrame(master=root, width=300, height=300, corner_radius=0, fg_color='#0b304a' )
frame02.grid(row = 0, column = 1)

btn1 = CTkButton(master=frame01, text='Botao 1', )
btn1.grid(row = 0, column = 0)



btn2 = CTkButton(master=frame01, text='Botao 2', )
btn2.grid(row = 1, column = 0)
root.mainloop()