import tkinter as tk
from tkinter import ttk


def enviar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    print(f"Nombre: {nombre}, Edad: {edad}")
    
ttk.Style().theme_use('winnative')
    
ventana = tk.Tk()
ventana.title("Formulario de Datos")

label_nombre = ttk.Label(ventana, text="Nombre")
label_nombre.pack()
entry_nombre = ttk.Entry(ventana)
entry_nombre.pack()

label_edad = ttk.Label(ventana, text="Edad")
label_edad.pack()
entry_edad = ttk.Entry(ventana)
entry_edad.pack()

boton_enviar = ttk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.pack()

ventana.mainloop()