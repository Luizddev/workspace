import tkinter as tk
from tkinter import ttk

# Criando a janela principal
root = tk.Tk()
root.title("Interface Gráfica com Tkinter")
root.geometry("400x300")  # Definindo tamanho da janela

# Campo de entrada (Field Input)
tk.Label(root, text="Nome:").pack()
entry = tk.Entry(root)
entry.pack()

# Checkbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Opção 1", variable=checkbox_var)
checkbox.pack()

# Radio Button
radio_var = tk.StringVar(value="Opção1")
tk.Label(root, text="Escolha uma opção:").pack()
tk.Radiobutton(root, text="Opção 1", variable=radio_var, value="Opção1").pack()
tk.Radiobutton(root, text="Opção 2", variable=radio_var, value="Opção2").pack()

# Combobox (Select)
tk.Label(root, text="Selecione uma opção:").pack()
combobox = ttk.Combobox(root, values=["Opção1", "Opção2", "Opção3"])
combobox.current(0)  # Define a opção padrão
combobox.pack()

# Botão
def on_click():
    print("Botão clicado!")

button = tk.Button(root, text="Clique Aqui", command=on_click)
button.pack(pady=10)

# Iniciando o loop da interface
root.mainloop()