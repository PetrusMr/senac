from customtkinter import *

def frame2 ():
    frame03.grid_forget()
    frame02.grid(row = 0, column = 1)

def frame3 ():
    frame02.grid_forget()
    frame03.grid(row = 0, column = 1)


root = CTk()
root.geometry('600x300')

frame01 = CTkFrame(master=root, width=300, height=300, corner_radius= 0, )
frame01.pack_propagate(False)
frame01.grid(row = 0, column = 0)


frame02 = CTkFrame(master=root, width=300, height=300, corner_radius=0, fg_color='#0b304a' )

frame03 = CTkFrame(master=root, width=300, height=300, corner_radius= 0, fg_color='#7a47ce')


btn1 = CTkButton(master=frame01, text='Botao 1', command= frame2 )
btn1.pack(pady=5)

btn2 = CTkButton(master=frame01, text='Botao 2', command= frame3 )
btn2.pack()

root.mainloop()