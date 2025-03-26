import customtkinter as ctk

def adicionar_valores():
    valor1 = "Valor 1"
    valor2 = "Valor 2"
    entry.insert("end", f"{valor1} {valor2}")  # Adiciona os valores juntos

# Configuração da interface
ctk.set_appearance_mode("dark")  # Modo escuro opcional
root = ctk.CTk()
root.geometry("300x200")

# Criando o Entry
entry = ctk.CTkEntry(root, width=200)
entry.pack(pady=10)

# Botão para adicionar valores
btn = ctk.CTkButton(root, text="Adicionar", command=adicionar_valores)
btn.pack(pady=10)

root.mainloop()