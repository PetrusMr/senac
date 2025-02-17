from customtkinter import *

root = CTk()


my_frame = CTkScrollableFrame(root)
my_frame.pack(pady=40)

nomes = [
    "Ana", "Carlos", "Julia", "Pedro", "Maria", 
    "Lucas", "Fernanda", "Gabriel", "Amanda", "Rafael", 
    "Isabela", "Tiago", "Camila", "Ricardo", "Larissa", 
    "Marcos", "Beatriz", "Mateus", "Juliana", "Diego"
]


var1 = 
  
r1=CTkRadioButton(my_frame, text='aa', value=1).pack(pady=12)
r2=CTkRadioButton(my_frame, text='b', value=2).pack(pady=12)
r3=CTkRadioButton(my_frame, text='c', value=3).pack(pady=12)
r4=CTkRadioButton(my_frame, text='d', value=4).pack(pady=12)
r5=CTkRadioButton(my_frame, text='e', value=5).pack(pady=12)
r6=CTkRadioButton(my_frame, text='f', value=6).pack(pady=12)

root.mainloop()

