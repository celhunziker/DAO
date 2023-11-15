from tkinter import *
from tkinter import messagebox, ttk
from logica import *



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
    menu_socios.add_command(label="Eliminar socio", command=eliminar_socio)
    menu_socios.add_command(label="Consultar socio", command=consultar_socios)

    menu_libros.add_command(label="Registrar libro", command=registrar_libro)
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


def validar_numeros(entrada):
    if entrada.isdigit() or entrada == "":
        return True
    else:
        return False

def registrar_libro():
    ventana_registrar_libro = Toplevel()
    ventana_registrar_libro.title("Registrar libro")
    ventana_registrar_libro.geometry("500x200")
    
    label_titulo = Label(ventana_registrar_libro, text="Registrar un libro", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    # Variable para la entrada
    numero_var = StringVar()
    validacion = ventana_registrar_libro.register(validar_numeros)

    label_codigo = Label(ventana_registrar_libro, text="Codigo:")
    label_codigo.grid(column=0, row=1)
    entry_codigo = Entry(ventana_registrar_libro, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_codigo.grid(column=1, row=1)
    label_titulo_libro = Label(ventana_registrar_libro, text="Titulo:")
    label_titulo_libro.grid(column=0,row=2)
    entry_titulo_libro = Entry(ventana_registrar_libro)
    entry_titulo_libro.grid(column=1,row=2)
    label_precio_repo = Label(ventana_registrar_libro, text="Precio de reposición:")
    label_precio_repo.grid(column=0,row=3)
    entry_precio_repo = Entry(ventana_registrar_libro)
    entry_precio_repo.grid(column=1,row=3)
    label_estado = Label(ventana_registrar_libro, text="Estado:")
    label_estado.grid(column=0,row=4)
    estados = ["DISPONIBLE", "PRESTADO", "EXTRAVIADO"]
    combo_estado = ttk.Combobox(ventana_registrar_libro, values=estados, state="readonly")
    combo_estado.grid(column=1,row=4)

    boton_registrar_libro = Button(ventana_registrar_libro, text="Registrar", command= lambda: boton_registrar_libro(ventana_registrar_libro, entry_codigo.get(), entry_titulo_libro.get(), entry_precio_repo.get(), combo_estado.get()))
    boton_registrar_libro.grid(column=1,row=6)

def consultar_socios():
    ventana_consultar_socio = Toplevel()
    ventana_consultar_socio.title("Consultar socio")
    ventana_consultar_socio.geometry("300x150")

    label_titulo = Label(ventana_consultar_socio, text="Consultar un socio", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    # Variable para la entrada
    numero_var = StringVar()
    validacion = ventana_consultar_socio.register(validar_numeros)
    
    label_numero_socio = Label(ventana_consultar_socio, text="Numero de socio:")
    label_numero_socio.grid(column=0,row=2)
    entry_numero_socio = Entry(ventana_consultar_socio, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_numero_socio.grid(column=1,row=2)

    boton_consultar = Button(ventana_consultar_socio, text="Consultar", command=lambda: boton_consultar_socio(ventana_consultar_socio, entry_numero_socio.get()))
    boton_consultar.grid(column=0, row=3)

def eliminar_socio():
    ventana_eliminar_socio = Toplevel()
    ventana_eliminar_socio.title("Eliminar socio")
    ventana_eliminar_socio.geometry("300x150")

    label_titulo = Label(ventana_eliminar_socio, text="Eliminar un socio", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    # Variable para la entrada
    numero_var = StringVar()
    validacion = ventana_eliminar_socio.register(validar_numeros)
    
    label_numero_socio = Label(ventana_eliminar_socio, text="Numero de socio:")
    label_numero_socio.grid(column=0,row=2)
    entry_numero_socio = Entry(ventana_eliminar_socio, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_numero_socio.grid(column=1,row=2)

    boton_eliminar = Button(ventana_eliminar_socio, text="Eliminar", command=lambda: boton_eliminar_socio(entry_numero_socio.get()))
    boton_eliminar.grid(column=0, row=3)

def registrar_socio():
    ventana_registro_socio = Toplevel()
    ventana_registro_socio.title("Registrar socio")
    ventana_registro_socio.geometry("300x150")

    label_titulo = Label(ventana_registro_socio, text="Registrar un socio", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    # Variable para la entrada
    numero_var = StringVar()
    validacion = ventana_registro_socio.register(validar_numeros)

    label_nombre = Label(ventana_registro_socio, text="Nombre:")
    label_nombre.grid(column=0,row=2)
    entry_nombre = Entry(ventana_registro_socio)
    entry_nombre.grid(column=1,row=2)
    label_numero_socio = Label(ventana_registro_socio, text="Numero de socio:")
    label_numero_socio.grid(column=0,row=3)
    entry_numero_socio = Entry(ventana_registro_socio, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_numero_socio.grid(column=1,row=3)
    boton_registrar = Button(ventana_registro_socio, text="Registrar", command=lambda: boton_registrar_socio(ventana_registro_socio, entry_numero_socio.get(), entry_nombre.get()))
    boton_registrar.grid(column=0,row=5)
    
    
    ventana_registro_socio.mainloop()

def boton_registrar_libro(ventana : Tk, codigo : str, titulo : str, precio : str, estado : str):
    try:
        if codigo and titulo and precio and estado:
            registrarLibro(codigo, titulo, precio, estado)
            mostrar_cartel_exitoso()
            ventana.destroy()
            registrar_socio()
        else:
            label_faltan_datos = Label(ventana, text="Completar todos los datos", fg="red")
            label_faltan_datos.grid(column=0,row=4)
    except:
        messagebox.showerror("Error", "El codigo ya se encuentra registrado")

def boton_consultar_socio(ventana : Tk, numero_socio : str):
    try:
        socio = consultarSocio(numero_socio)
        label_retorno_consulta = Label(ventana, text=f"SOCIO/A {socio.nombre} NÚMERO {socio.numeroSocio}")
        label_retorno_consulta.grid(column=0,row=4)
    except:
        messagebox.showerror("Error", "El socio no existe")

def boton_eliminar_socio(numero_socio : str):
    try:
        socio = consultarSocio(numero_socio)
        respuesta = messagebox.askokcancel("Confirmar", f"¿Desea eliminar al socio {socio.nombre}?")
        if respuesta:
            eliminarSocio(socio)
            messagebox.showinfo("Éxito", "Se eliminó correctamente")
    except:
        messagebox.showerror("Error", "El socio no existe")

def mostrar_cartel_exitoso():
    messagebox.showinfo("Éxito", "Registro exitoso")

def boton_registrar_socio(ventana, numero_socio, nombre):
    try:
        if numero_socio and nombre:
            registrarSocio(nombre, numero_socio)
            mostrar_cartel_exitoso()
            ventana.destroy()
            registrar_socio()
        else:
            label_faltan_datos = Label(ventana, text="Completar todos los datos", fg="red")
            label_faltan_datos.grid(column=0,row=4)
    except NroSocioExistente:
        messagebox.showerror("Error","El numero de socio ya existe")

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