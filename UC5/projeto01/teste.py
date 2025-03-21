from customtkinter import *

def salvar_texto(event):
    texto = ent.get()
    print(texto)


root = CTk()

ent = CTkEntry(root)
ent.pack()



ent.bind("<KeyRelease>", salvar_texto)
root.mainloop()




