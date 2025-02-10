from customtkinter import *

def executar():
    try:
        hrs = float(hrs_entry.get())
        qntd_horas = float(qntd_horas_entry.get())
    except ValueError:
        return  

    bruto = hrs * qntd_horas
    inss = bruto * 0.1
    fgts = bruto * 0.11
    sindicato = bruto * 0.03  

    # Criar nova janela
    root2 = CTkToplevel(master=root)
    root2.geometry('500x400')
    root2.title('Cálculo de salário')
    root2.resizable(False, False)
    root2.attributes('-topmost', True)

    frame1 = CTkFrame(master=root2, width=300, height=400)
    frame1.pack(pady=10)

    lb_titulo = CTkLabel(master=frame1, text='Resultado', font=("Arial", 16, "bold"))
    lb_titulo.pack(pady=10)

    frame2 = CTkFrame(master=frame1, width=280, height=200)
    frame2.pack(pady=10)

    
    if bruto <= 900:
        ir = 0
        faixa_ir = "0%"
    elif bruto <= 1500:
        ir = bruto * 0.05
        faixa_ir = "5%"
    elif bruto <= 2500:
        ir = bruto * 0.1
        faixa_ir = "10%"
    else:
        ir = bruto * 0.2
        faixa_ir = "20%"

    total_descontos = ir + inss + sindicato
    salario_liquido = bruto - total_descontos

    labels = ["Salário Bruto:", "IR (" + faixa_ir + "):", "INSS (10%):", "FGTS (11%):", "Total Descontos:", "Salário Líquido:"]
    valores = [bruto, ir, inss, fgts, total_descontos, salario_liquido]

    for i, (label, valor) in enumerate(zip(labels, valores)):
        CTkLabel(master=frame2, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = CTkEntry(master=frame2, width=120)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, f"R$ {valor:.2f}")
        entry.configure(state="disabled")  
        


set_appearance_mode('Dark')

root = CTk()
root.geometry('500x400')
root.title('Cálculo de Salário')
root.resizable(False, False)

frame_base = CTkFrame(master=root, width=300, height=400)
frame_base.pack(pady=20)

titulo_label = CTkLabel(master=frame_base, text='Calculadora de Imposto', font=("Arial", 16, "bold"))
titulo_label.pack(pady=10)

hrs_entry = CTkEntry(master=frame_base, placeholder_text='Valor da hora Trabalhada')
hrs_entry.pack(pady=5)

qntd_horas_entry = CTkEntry(master=frame_base, placeholder_text='Quantidade de horas trabalhadas')
qntd_horas_entry.pack(pady=5)

btn_confirmar = CTkButton(master=frame_base, text='Confirmar', command=executar)
btn_confirmar.pack(pady=10)

root.mainloop()
