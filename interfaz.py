import tkinter
from tkinter import *

def inicio():
    ventana = Tk()
    ventana.title("Gestión de biblioteca")
    ventana.geometry("800x500")

    agregar_menu(ventana)
    ventana.mainloop()

def agregar_menu(ventana : Tk):
    barra_menu = Menu(ventana)
    ventana.config(menu=barra_menu)

    menu_socios = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de socios", menu=menu_socios)
    menu_libros = Menu(barra_menu)
    barra_menu.add_cascade(label="Administración de libros", menu=menu_libros)
    menu_prestamos_devoluc = Menu(barra_menu)
    barra_menu.add_cascade(label="Registración de préstamos y devoluciones", menu=menu_prestamos_devoluc)
    barra_menu.add_command(label="Registración de libros extraviados", command=x)
    menu_reportes = Menu(barra_menu)
    barra_menu.add_cascade(label="Reportes", menu=menu_reportes)

    menu_socios.add_command(label="Registrar socio", command=registrar_socio)
    menu_socios.add_command(label="Eliminar socio", command=x)
    menu_socios.add_command(label="Consultar socio", command=x)

    menu_libros.add_command(label="Registrar libro", command=x)
    menu_libros.add_command(label="Eliminar libro", command=x)
    menu_libros.add_command(label="Consultar libro", command=x)

    menu_prestamos_devoluc.add_command(label="Registrar prestamo", command=x)
    menu_prestamos_devoluc.add_command(label="Registrar devolución", command=x)

    menu_reportes.add_command(label="Cantidad de libros en cada estado (tres totales)",command=x)
    menu_reportes.add_command(label="Sumatoria del precio de reposición de todos los libros extraviados",command=x)
    menu_reportes.add_command(label="Nombre de todos los solicitantes de un libro en particular identificado por su título",command=x)
    menu_reportes.add_command(label="Listado de préstamos de un socio identificado por su número de socio",command=x)
    menu_reportes.add_command(label="Listado de préstamos demorados",command=x)

def x():
    pass

def limpiar_ventana(ventana : Tk):
    for widget in ventana.winfo_children():
        widget.destroy()

def registrar_socio():
    ventana_registro_socio = Toplevel()
    ventana_registro_socio.title("Registrar socio")
    ventana_registro_socio.geometry("300x150")

    label_titulo = Label(ventana_registro_socio, text="Registrar un socio", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    label_nombre = Label(ventana_registro_socio, text="Nombre:")
    label_nombre.grid(column=0,row=2)
    entry_nombre = Entry(ventana_registro_socio)
    entry_nombre.grid(column=1,row=2)
    boton_registrar = Button(ventana_registro_socio, text="Registrar", command=boton_registrar_socio)
    boton_registrar.grid(column=0,row=3)

    ventana_registro_socio.mainloop()

def eliminar_socio():
    pass
def consultar_socio():
    pass

def boton_registrar_socio():
    pass
"""
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
"""