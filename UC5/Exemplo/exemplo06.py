from customtkinter import *

v_notas = []
maior_media = 0
menor_media = 0
conta_alunos = 0

def continha():
     for i in range(0,len(v_notas)):
        
        if  v_notas[i] >=7:
            maior_media +=1
        else:
            menor_media +=1

def salvar():
    global notas, v_notas, conta_alunos
    conta_alunos +=1
    lb_qtd_alunos.configure(text= f'Quantidades de alunos: {conta_alunos}')
    notas=(float(n1.get())+ float(n2.get())+ float(n3.get())+ float(n4.get())) /4
    v_notas.append(notas)  

    n1.delete(0,END)
    n2.delete(0,END)
    n3.delete(0, END)
    n4.delete(0,END)
    
def resultado():
    global v_notas, maior_media, menor_media, conta_alunos
    continha()
    
    root2 = CTkToplevel()
    root2.attributes('-topmost', True)
    lab_2 = CTkLabel(master=root2, text=f'Maior ou igual a 7')
    lab_2.grid(row=1, column=1, sticky="w")


    lab_3 = CTkLabel(master=root2, text='menor que 7 ')
    lab_3.grid(row=2,column=1, sticky='w')

    entry1 = CTkEntry(master=root2, )
    entry1.grid(row=1, column=2,padx=12,sticky="e")
    entry2 = CTkEntry(master= root2,)
    entry2.grid(row=2, column=2, padx= 12,sticky = 'e')

    entry2.insert(0,f'{menor_media}')
    entry1.insert(0,f'{maior_media}')

    entry1.configure(state="disabled")
    entry2.configure(state="disabled")
    # conf_Btn.configure(state = 'disabled')
    v_notas.clear()
    maior_media = 0
    menor_media = 0
    conta_alunos = 0
    lb_qtd_alunos.configure(text= f'Quantidades de alunos: {conta_alunos}')
    root2.mainloop()

root = CTk()
root.geometry('500x400')
root.title('Calculo de media')
root.resizable(FALSE, False)

frame_base = CTkFrame(master=root, width=300, height=400)
frame_base.pack(pady=20)


lb_Titulo = CTkLabel(master=frame_base, text='Insira as notas')
lb_Titulo.pack(pady=20, padx= 10)
lb_qtd_alunos = CTkLabel(master=frame_base, text='')
lb_qtd_alunos.pack()

n1 = CTkEntry(master=frame_base, placeholder_text='NOTA 1')
n1.pack(pady=5)
n2 = CTkEntry(master=frame_base, placeholder_text='NOTA 2')
n2.pack(pady=10, padx= 30)
n3 = CTkEntry(master=frame_base, placeholder_text='NOTA 3')
n3.pack(pady=10, padx= 10)
n4 = CTkEntry(master=frame_base, placeholder_text='NOTA 4')
n4.pack(pady=10, padx= 10)

conf_Btn = CTkButton(master=frame_base, text='Salvar', command=salvar)
conf_Btn.pack(pady= 15)



r_Btn = CTkButton(master=frame_base, text='Resultado', command=resultado)
r_Btn.pack()

root.mainloop()