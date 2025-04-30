import tkinter as tk
from tkinter import ttk, messagebox

# Superclase
class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio:.1f}"

# Subclase Palco
class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

# Subclase Platea
class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.precio = 50.0 if dias_anticipacion >= 10 else 60.0

# Subclase Galería
class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.precio = 50.0 if dias_anticipacion >= 10 else 30.0

# Función que se ejecuta al presionar "Vende"
def vender_boleto():
    tipo = tipo_boleto.get()
    try:
        numero = int(entry_numero.get())
        dias = int(entry_dias.get())
    except ValueError:
        messagebox.showerror("Error", "Número de boleto y días deben ser enteros.")
        return

    if tipo == "Palco":
        boleto = Palco(numero)
    elif tipo == "Platea":
        boleto = Platea(numero, dias)
    elif tipo == "Galería":
        boleto = Galeria(numero, dias)
    else:
        messagebox.showerror("Error", "Debe seleccionar un tipo de entrada.")
        return

    etiqueta_info.config(text=str(boleto))

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Teatro Municipal")
ventana.geometry("400x300")

# Título
titulo = tk.Label(ventana, text="Teatro Municipal", font=("Arial", 16))
titulo.pack(pady=10)

# Frame para los datos del boleto
frame = tk.Frame(ventana)
frame.pack(pady=5)

tipo_boleto = tk.StringVar()

tk.Label(frame, text="Tipo de entrada:").grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame, text="Palco", variable=tipo_boleto, value="Palco").grid(row=0, column=1)
tk.Radiobutton(frame, text="Platea", variable=tipo_boleto, value="Platea").grid(row=0, column=2)
tk.Radiobutton(frame, text="Galería", variable=tipo_boleto, value="Galería").grid(row=0, column=3)

tk.Label(frame, text="Número:").grid(row=1, column=0, sticky="w", pady=5)
entry_numero = tk.Entry(frame)
entry_numero.grid(row=1, column=1)

tk.Label(frame, text="Días antes del evento:").grid(row=2, column=0, sticky="w")
entry_dias = tk.Entry(frame)
entry_dias.grid(row=2, column=1)

# Botones
boton_vende = tk.Button(ventana, text="Vende", command=vender_boleto)
boton_vende.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
boton_salir.pack()

# Área de información
etiqueta_info = tk.Label(ventana, text="Información", font=("Arial", 12), fg="blue")
etiqueta_info.pack(pady=10)

ventana.mainloop()