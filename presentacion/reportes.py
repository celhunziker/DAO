from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generar_reporte_libros_x_estado(lista):
    # Crear un documento PDF
    doc = SimpleDocTemplate("informe_con_grafico.pdf", pagesize=letter)
    # Crear una lista de elementos para agregar al informe
    elements = []

    # Agregar un título al informe
    elements.append(Paragraph("Informe Biblioteca"))
    elements.append(Spacer(1, 12))
    # Agregar un subtítulo
    elements.append(Paragraph("Gráfico de estado de los libros de la biblioteca"))
    elements.append(Spacer(1, 12))

    # Datos para el gráfico
    data = [int(tupla[1]) for tupla in lista]
    labels = [tupla[0] for tupla in lista]
    # Crear un gráfico de tarta con Matplotlib
    plt.pie(data, labels=labels, autopct='%1.1f%%')
    plt.axis('equal') # Aspecto igual para que sea un círculo
    
    # Guardar el gráfico en un búfer de BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Agregar el gráfico al informe como una imagen
    elements.append(Image(buffer, width=300, height=300))
    elements.append(Spacer(1, 12))
    # Cerrar el documento PDF
    doc.build(elements)

    import subprocess
    subprocess.Popen(["grafico_reportlab.pdf"], shell=True)


def reporte_precio_extraviados(sumatoria):
    # Crear un documento PDF
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)

    # Crear una lista para almacenar los elementos del informe
    elements = []

    # Crear estilos para el informe
    styles = getSampleStyleSheet()

    # Agregar un título
    title = "Sumatoria del precio de reposición los libros extraviados "
    elements.append(Paragraph(title, styles['Title']))

    # Agregar una tabla de ejemplo
    data = ["Total sumatoria", sumatoria]
    
    table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)

def generar_reporte_prestamos_x_socio(listaPrestamos: list, nroSocio: str):
    # Crear un documento PDF
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)

    # Crear una lista para almacenar los elementos del informe
    elements = []

    # Crear estilos para el informe
    styles = getSampleStyleSheet()

    # Agregar un título
    title = "Prestamos solicitados por el socio: " + nroSocio
    elements.append(Paragraph(title, styles['Title']))

    # Agregar una tabla de ejemplo
    #for lista in listaPrestamos:
    data = listaPrestamos
        #data.append([lista[0], lista[1], lista[3], lista[4], lista[5], lista[6], lista[7]])
    
    table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)

def generar_reporte_solic_de_titulo(lista_solicitantes, titulo):
    
    # Crear un documento PDF
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)

    # Crear una lista para almacenar los elementos del informe
    elements = []

    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = f"Solicitantes del titulo {titulo}"
    elements.append(Paragraph(title, styles['Title']))
    # Agregar un párrafo de text
    text = f"Este informe muestra las personas que han solicitado el libro ."
    elements.append(Paragraph(text, styles['Normal']))
    # Agregar una tabla de ejemplo
    data = lista_solicitantes
    table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)

def generar_reporte_prest_demorados(lista_demorados)

    # Crear un documento PDF
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)

    # Crear una lista para almacenar los elementos del informe
    elements = []

    # Crear estilos para el informe
    styles = getSampleStyleSheet()
    # Agregar un título
    title = f"Listado de Prestamos demorados"
    elements.append(Paragraph(title, styles['Title']))
    
    # Agregar una tabla de ejemplo
    data = lista_demorados
    table = Table(data, colWidths=[1 * inch, 1 * inch, 1 * inch])
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)
    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)