from customtkinter import *

def switch_event():
   
    if switch.get():  
        frame02.grid_forget()  
        frame03.grid(row=0, column=1)  
    else: 
        frame03.grid_forget()  
        frame02.grid(row=0, column=1)  
root = CTk()
root.geometry('600x300')

frame01 = CTkFrame(master=root, width=300, height=300, corner_radius=0)
frame01.pack_propagate(False)
frame01.grid(row=0, column=0)

frame02 = CTkFrame(master=root, width=300, height=300, corner_radius=0, fg_color='#0b304a')
frame03 = CTkFrame(master=root, width=300, height=300, corner_radius=0, fg_color='#7a47ce')

switch = CTkSwitch(master=frame01, command=switch_event, text='SWITCH')
switch.pack()

root.mainloop()
