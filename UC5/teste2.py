from PIL import Image, ImageTk
from customtkinter import *

import os
file_path = os.path.dirname(os.path.realpath(__file__))
image1 = CTkImage(Image.open(fp= "C:/Users/970548/OneDrive - SENAC em Minas - EDU/Documentos/Senac/senac/UC5/projeto01/lixeira.png"), size=(35,35))

app = CTk()

btn = CTkButton(master=app, image=image1, text='')
btn.pack()
app.mainloop()
