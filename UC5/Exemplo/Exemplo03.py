from customtkinter import *

def Calcular ():
    peso = float(entry_peso.get())
    altura = float(entry_Altura.get())
    IMC = peso / (altura **2)

    lb_IMC.configure(text = 'IMC: {:,.2f}'.format(IMC))


    if IMC <18.5:
        lb_Info_IMC.configure(text= 'Classificação: Magreza') 

    elif IMC < 24.9:
        lb_Info_IMC.configure(text= 'Classificação: Normal')

    elif IMC < 29.9:
        lb_Info_IMC.configure(text= 'Classificação: SobrePeso')
    
    elif IMC < 34.9:
        lb_Info_IMC.configure(text= 'Classificação: Obesidade I') 
    
    elif IMC < 39.9:
        lb_Info_IMC.configure(text= 'Classificação: Obesidade II') 

    else: 
        lb_Info_IMC.configure(text= 'Classificação: Obesidade III') 

        



set_appearance_mode('Dark')
root = CTk()
root.title('Calculadora de IMC')
root.geometry('400x400')
root.resizable(FALSE, False)

lb_titulo = CTkLabel(master=root, text='Calculadora de IMC', font=('Arial',20))
lb_titulo.pack(pady=15)

entry_peso = CTkEntry(master=root, placeholder_text='Peso (kg)', width=200, border_color='#16e7a1', border_width=2)
entry_peso.pack(pady=10)

entry_Altura = CTkEntry(master=root, placeholder_text='Altura (m)', width=200,  border_color='#16e7a1', border_width=2)
entry_Altura.pack()

btn = CTkButton(master=root, text='Calcular', command= Calcular,  fg_color='#16e7a1', text_color='black', corner_radius=32, hover_color='#9216e7')
btn.pack(pady=25)

lb_IMC = CTkLabel(master=root, text='', font=('Arial', 20))
lb_IMC.pack(pady=10)

lb_Info_IMC = CTkLabel(master=root, text='', font=('Arial', 20))
lb_Info_IMC.pack()

root.mainloop()