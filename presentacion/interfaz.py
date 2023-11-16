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
    menu_libros.add_command(label="Eliminar libro", command=eliminar_libro)
    menu_libros.add_command(label="Consultar libro", command=consultar_libro)

    menu_prestamos_devoluc.add_command(label="Registrar prestamo", command=registrar_prestamo)
    menu_prestamos_devoluc.add_command(label="Registrar devolución", command=registrar_devolucion)

    menu_reportes.add_command(label="Cantidad de libros en cada estado (tres totales)",command=generar_reporte_libros_x_estado)
    menu_reportes.add_command(label="Sumatoria del precio de reposición de todos los libros extraviados",command=generar_reporte_sum_precio_extraviados)
    menu_reportes.add_command(label="Nombre de todos los solicitantes de un libro en particular identificado por su título",command=buscar_solic_x_titulo)
    menu_reportes.add_command(label="Listado de préstamos de un socio identificado por su número de socio",command=buscar_prestamo_x_nroSocio)
    menu_reportes.add_command(label="Listado de préstamos demorados",command=generar_reporte_prestamos_demorados)

def x():
    pass


def validar_numeros(entrada):
    if entrada.isdigit() or entrada == "":
        return True
    else:
        return False

def validar_numeros_coma(valor):
    # Permite solo números y una coma en el Entry
    return valor == "" or (valor.replace(",", "").replace(".", "").isdigit() and valor.count(",") <= 1)

def buscar_solic_x_titulo():
    ventana_titulo_libro = Toplevel()
    ventana_titulo_libro.title("Reporte de solicitantes de un libro")
    ventana_titulo_libro.geometry("500x500")
    
    label_titulo = Label(ventana_titulo_libro, text="Reporte de solicitantes", font=("Arial bold", 12))
    label_titulo.pack(pady=5)

    label_titulo_libro = Label(ventana_titulo_libro, text="Titulo:")
    label_titulo_libro.pack(pady=5)
    entry_titulo_libro = Entry(ventana_titulo_libro)
    entry_titulo_libro.pack(pady=5)
    
    boton_titulo_libro = Button(ventana_titulo_libro, text="Consultar", command= lambda: mostrar_solicitantes(ventana_titulo_libro, entry_titulo_libro.get()))
    boton_titulo_libro.pack(pady=5)

    boton_generar_reporte = Button(ventana_titulo_libro, text="Generar reporte", command= lambda: generar_reporte_solic_x_titulo(entry_titulo_libro.get()))
    boton_generar_reporte.pack(side= "bottom", pady=10)

def generar_reporte_solic_x_titulo(titulo):
    if titulo:
        lista_solicitantes = buscar_solicitantes(titulo)
        if len(lista_solicitantes) > 0:
            generar_reporte_solic_de_titulo(lista_solicitantes, titulo)

def buscar_solicitantes(titulo : str):
    listaSolicitantes = buscar_solicitantes_x_libro(titulo)
    return listaSolicitantes

def mostrar_solicitantes(ventana : Tk, titulo : str):
    if titulo:
        try:
            listaSolicitantes = buscar_solicitantes(titulo)
            if len(listaSolicitantes) > 0:
                columns = ("Número de Socio", "Nombre")
                tree = ttk.Treeview(ventana, columns=columns, show="headings")

                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)  

                    # Llenar la tabla con datos
                    for socio in listaSolicitantes:
                        tree.insert("", "end", values=(socio[0], socio[1]))

                    # Empaquetar la tabla
                    tree.pack(padx=10, pady=10)

                    return listaSolicitantes
        except LibroInexistente:
            messagebox.showerror("Error", f"No existen libros registrados con el titulo '{titulo}'")
    else:
        label_faltan_datos = Label(ventana, text="Ingresar un titulo", fg="red")
        label_faltan_datos.pack(side="bottom",pady=10)

def generar_reporte_libros_x_estado():
    generar_reporte_libros_x_est()

def generar_reporte_sum_precio_extraviados():
    generar_reporte_sum_precio_extra()

def generar_reporte_prestamos_demorados():
    generar_reporte_prestamos_demor()

def buscar_prestamo_x_nroSocio():
    ventana_prestamo_socio = Toplevel()
    ventana_prestamo_socio.title("Reporte de Prestamos de un socio")
    ventana_prestamo_socio.geometry("500x200")
    
    label_titulo = Label(ventana_prestamo_socio, text="Prestamos de un socio determinado", font=("Arial bold", 12))
    label_titulo.grid(column=0, row=0)
    
    nro_var = StringVar()

    label_nroSocio = Label(ventana_prestamo_socio, text="Numero de Socio:")
    label_nroSocio.grid(column=0, row=2)
    
    entry_nroSocio = Entry(ventana_prestamo_socio, textvariable=nro_var)
    entry_nroSocio.grid(column=1, row=2)     
    
    boton_nroSocio = Button(ventana_prestamo_socio, text="Consultar", command=lambda: generar_reporte_prestamo_x_socio(entry_nroSocio.get()))
    boton_nroSocio.grid(column=1, row=6)
    
'''
def registrar_libro():
    ventana_registrar_libro = Toplevel()
    ventana_registrar_libro.title("Registrar libro")
    ventana_registrar_libro.geometry("500x200")
    
    label_titulo = Label(ventana_registrar_libro, text="Registrar un libro", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    precio_var = StringVar()

    # Configurar validación
    validacion = ventana_registrar_libro.register(validar_numeros_coma)

    label_titulo_libro = Label(ventana_registrar_libro, text="Titulo:")
    label_titulo_libro.grid(column=0,row=2)
    entry_titulo_libro = Entry(ventana_registrar_libro)
    entry_titulo_libro.grid(column=1,row=2)
    label_precio_repo = Label(ventana_registrar_libro, text="Precio de reposición:")
    label_precio_repo.grid(column=0,row=3)
    entry_precio_repo = Entry(ventana_registrar_libro, textvariable=precio_var, validate="key", validatecommand=(validacion, "%P"))
    entry_precio_repo.grid(column=1,row=3)
    label_estado = Label(ventana_registrar_libro, text="Estado:")
    label_estado.grid(column=0,row=4)
    estados = ["DISPONIBLE", "PRESTADO", "EXTRAVIADO"]
    combo_estado = ttk.Combobox(ventana_registrar_libro, values=estados, state="readonly")
    combo_estado.grid(column=1,row=4)

    boton_registrar_libro = Button(ventana_registrar_libro, text="Registrar", command= lambda: boton_registrar_libro_accion(ventana_registrar_libro, entry_titulo_libro.get(), entry_precio_repo.get(), combo_estado.get()))
    boton_registrar_libro.grid(column=1,row=6)
'''


def generar_reporte_prestamo_x_socio(nroSocio: str):
    generar_reporte_prest_socios(nroSocio)


def registrar_libro():
    ventana_registrar_libro = Toplevel()
    ventana_registrar_libro.title("Registrar libro")
    ventana_registrar_libro.geometry("500x200")
    
    label_titulo = Label(ventana_registrar_libro, text="Registrar un libro", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    precio_var = StringVar()

    # Configurar validación
    validacion = ventana_registrar_libro.register(validar_numeros_coma)

    label_titulo_libro = Label(ventana_registrar_libro, text="Titulo:")
    label_titulo_libro.grid(column=0,row=2)
    entry_titulo_libro = Entry(ventana_registrar_libro)
    entry_titulo_libro.grid(column=1,row=2)
    label_precio_repo = Label(ventana_registrar_libro, text="Precio de reposición:")
    label_precio_repo.grid(column=0,row=3)
    entry_precio_repo = Entry(ventana_registrar_libro, textvariable=precio_var, validate="key", validatecommand=(validacion, "%P"))
    entry_precio_repo.grid(column=1,row=3)
    label_estado = Label(ventana_registrar_libro, text="Estado:")
    label_estado.grid(column=0,row=4)
    estados = ["DISPONIBLE", "PRESTADO", "EXTRAVIADO"]
    combo_estado = ttk.Combobox(ventana_registrar_libro, values=estados, state="readonly")
    combo_estado.grid(column=1,row=4)

    boton_registrar_libro = Button(ventana_registrar_libro, text="Registrar", command= lambda: boton_registrar_libro_accion(ventana_registrar_libro, entry_titulo_libro.get(), entry_precio_repo.get(), combo_estado.get()))
    boton_registrar_libro.grid(column=1,row=6)
    
def consultar_libro():
    ventana_consultar_libro = Toplevel()
    ventana_consultar_libro.title("Consultar libros")
    ventana_consultar_libro.geometry("600x300")

    label_titulo = Label(ventana_consultar_libro, text="Consultar libros", font=("Arial bold", 12))
    label_titulo.pack(pady=10)

    libros = listarLibros()
    columns = ("Codigo de libro", "Título", "Precio de reposición", "Estado")
    tree = ttk.Treeview(ventana_consultar_libro, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)  

    # Llenar la tabla con datos
    for libro in libros:
        tree.insert("", "end", values=(libro[0], libro[1], libro[2], libro[3]))

    # Empaquetar la tabla
    tree.pack(padx=10, pady=10)

    
def eliminar_libro():
    ventana_eliminar_libro = Toplevel()
    ventana_eliminar_libro.title("Eliminar libro")
    ventana_eliminar_libro.geometry("300x150")

    label_titulo = Label(ventana_eliminar_libro, text="Eliminar un libro", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    # Variable para la entrada
    numero_var = StringVar()
    validacion = ventana_eliminar_libro.register(validar_numeros)
    
    label_codigo = Label(ventana_eliminar_libro, text="Código de libro:")
    label_codigo.grid(column=0,row=2)
    entry_codigo = Entry(ventana_eliminar_libro, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_codigo.grid(column=1,row=2)

    boton_eliminar_libro = Button(ventana_eliminar_libro, text="Eliminar", command=lambda: boton_eliminar_libro_accion(entry_codigo.get()))
    boton_eliminar_libro.grid(column=0, row=3)

def consultar_socios():
    ventana_consultar_socio = Toplevel()
    ventana_consultar_socio.title("Consultar socio")
    ventana_consultar_socio.geometry("300x150")

    label_titulo = Label(ventana_consultar_socio, text="Consultar socios", font=("Arial bold", 12))
    label_titulo.pack(pady=10)

    socios = listarSocios()
    columns = ("Codigo de socio", "Nombre")
    tree = ttk.Treeview(ventana_consultar_socio, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)  

    # Llenar la tabla con datos
    if len(socios) > 0:
        for socio in socios:
            tree.insert("", "end", values=(socio[0], socio[1]))

    # Empaquetar la tabla
    tree.pack(padx=10, pady=10)

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

    boton_eliminar = Button(ventana_eliminar_socio, text="Eliminar", command=lambda: boton_eliminar_socio(ventana_eliminar_socio, entry_numero_socio.get()))
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
    boton_registrar = Button(ventana_registro_socio, text="Registrar", command=lambda: boton_registrar_socio(ventana_registro_socio, entry_nombre.get()))
    boton_registrar.grid(column=0,row=5)
    
    
    ventana_registro_socio.mainloop()

# revisar 
def registrar_prestamo():
    ventana_registrar_prestamo = Toplevel()
    ventana_registrar_prestamo.title("Registrar prestamo")
    ventana_registrar_prestamo.geometry("300x150")

    label_titulo = Label(ventana_registrar_prestamo, text="Registrar un prestamo", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)
    
    # Variable para la entrada
    numero_var = StringVar()
    numero_var1 = StringVar()
    validacion = ventana_registrar_prestamo.register(validar_numeros)
    
    # codigo de libro 
    label_libro = Label(ventana_registrar_prestamo, text="Codigo Libro:")
    label_libro.grid(column=0,row=2)
    entry_libro = Entry(ventana_registrar_prestamo, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_libro.grid(column=1,row=2)
    # nro de socio 
    label_nroSocio = Label(ventana_registrar_prestamo, text="Numero Socio:")
    label_nroSocio.grid(column=0,row=3)
    entry_nroSocio = Entry(ventana_registrar_prestamo, textvariable=numero_var1, validate="key", validatecommand=(validacion, "%P"))
    entry_nroSocio.grid(column=1,row=3)
    # dias 
    label_diasPrestamo = Label(ventana_registrar_prestamo, text="Dias Prestamo:")
    label_diasPrestamo.grid(column=0,row=4)
    entry_diasPrestamo = Entry(ventana_registrar_prestamo)
    entry_diasPrestamo.grid(column=1,row=4)

    boton_registrar_prestamo = Button(ventana_registrar_prestamo, text="Registrar", command=lambda: boton_registrar_prestamo_accion(ventana_registrar_prestamo, entry_libro.get(), entry_nroSocio.get(), entry_diasPrestamo.get()))
    boton_registrar_prestamo.grid(column=0,row=5)

def registrar_devolucion():
    ventana_registro_devolucion = Toplevel()
    ventana_registro_devolucion.title("Registrar devolucion")
    ventana_registro_devolucion.geometry("300x150")

    label_titulo = Label(ventana_registro_devolucion, text="Registrar una devolucion", font=("Arial bold", 12))
    label_titulo.grid(column=0,row=0)

    # Variable para la entrada
    numero_var = StringVar()
    validacion = ventana_registro_devolucion.register(validar_numeros)

    label_idPrestamo = Label(ventana_registro_devolucion, text="Id Prestamo:")
    label_idPrestamo.grid(column=0,row=2)
    entry_idPrestamo = Entry(ventana_registro_devolucion, textvariable=numero_var, validate="key", validatecommand=(validacion, "%P"))
    entry_idPrestamo.grid(column=1,row=2)
    boton_registrar_devolucion = Button(ventana_registro_devolucion, text="Registrar", command=lambda: boton_registrar_devolucion_accion(ventana_registro_devolucion, entry_idPrestamo.get()))
    boton_registrar_devolucion.grid(column=0,row=5)
    
    
    ventana_registro_devolucion.mainloop()



def boton_registrar_libro_accion(ventana : Tk, titulo : str, precio : str, estado : str):
    try:
        if titulo and precio and estado:
            registrarLibro(titulo, precio, estado)
            mostrar_cartel_exitoso()
            ventana.destroy()
        else:
            label_faltan_datos = Label(ventana, text="Completar todos los datos", fg="red")
            label_faltan_datos.grid(column=0,row=4)
    except:
        messagebox.showerror("Error", "El codigo ya se encuentra registrado")
        
def boton_consultar_libro_accion(ventana : Tk, codigo : str):
    try:
        libro = consultarLibro(codigo)
        label_retorno_consulta = Label(ventana, text=f"Libro {libro.titulo} Código {libro.codigo}")
        label_retorno_consulta.grid(column=0,row=4)
    except:
        messagebox.showerror("Error", "El libro no existe")
        
def boton_eliminar_libro_accion(codigo : str):
    try:
        libro = consultarLibro(codigo)
        respuesta = messagebox.askokcancel("Confirmar", f"¿Desea eliminar al libro {libro.titulo}?")
        if respuesta:
            eliminarLibro(libro)
            messagebox.showinfo("Éxito", "Se eliminó correctamente")
    except:
        messagebox.showerror("Error", "El libro no existe")

def boton_consultar_socio(ventana : Tk, numero_socio : str):
    try:
        socio = consultarSocio(numero_socio)
        label_retorno_consulta = Label(ventana, text=f"SOCIO/A {socio.nombre} NÚMERO {socio.numeroSocio}")
        label_retorno_consulta.grid(column=0,row=4)
    except:
        messagebox.showerror("Error", "El socio no existe")

def boton_eliminar_socio(ventana, numero_socio : str):
    try:
        socio = consultarSocio(numero_socio)
        respuesta = messagebox.askokcancel("Confirmar", f"¿Desea eliminar al socio {socio.nombre}?")
        if respuesta:
            eliminarSocio(socio)
            messagebox.showinfo("Éxito", "Se eliminó correctamente")
            ventana.destroy()
    except:
        messagebox.showerror("Error", "El socio no existe")

def mostrar_cartel_exitoso():
    messagebox.showinfo("Éxito", "Registro exitoso")

def boton_registrar_socio(ventana, nombre):
    if nombre:
        registrarSocio(nombre)
        mostrar_cartel_exitoso()
        ventana.destroy()
    else:
        label_faltan_datos = Label(ventana, text="Completar todos los datos", fg="red")
        label_faltan_datos.grid(column=0,row=4)


# revisar delfi 
def boton_registrar_prestamo_accion(ventana : Tk, codigoLibro: str, nroSocio : str, dias : str):
    try:
        if codigoLibro and nroSocio and dias:
                try:
                    registrarPrestamo(codigoLibro, nroSocio, dias)
                    mostrar_cartel_exitoso()
                    ventana.destroy()
                except LibroNoDisponible: 
                    messagebox.showerror("Error","El libro no esta disponible")
        else:
                label_faltan_datos = Label(ventana, text="Completar todos los datos", fg="red")
                label_faltan_datos.grid(column=0,row=4)
    except (NroSocioInxistente, LibroInexistente,) as e:
            messagebox.showerror("Error","El socio o libro no existen")
    

def boton_registrar_devolucion_accion(ventana : Tk, idPrestamo: str):
    try:
        if idPrestamo:
                registrarDevolucion(idPrestamo)
                mostrar_cartel_exitoso()
                ventana.destroy()
        else:
                label_faltan_datos = Label(ventana, text="Completar todos los datos", fg="red")
                label_faltan_datos.grid(column=0,row=4)
    except PrestamoInexistente:
            messagebox.showerror("Error","El prestamo no existe")

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