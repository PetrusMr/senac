from customtkinter import *

root =CTk()
root.geometry('500x300')


num1 = 130
num2 = 24
num3 = 67834
num4 = 5874
num5 = 4123


texto_label = f"{'Numero1':<10} : {num1:>10}\n{'Numero2':<10} : {num2:>10}\n{'Numero3':<10} : {num3:>10}\n{'Numero4':<10} : {num4:>10}\n{'Numero5':<10} : {num5:>10}"

label = CTkLabel(master=root, text=texto_label, font=("Consolas",28))
label.pack(pady=50)


root.mainloop()