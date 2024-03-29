import os
from reportlab.pdfgen import canvas
from PyQt5 import QtSql
from datetime import datetime
from img import var


class Informes:
    def listadoClientes(self):
        try:
            var.cv = canvas.Canvas('informes/listadoclientes.pdf')
            var.cv.setTitle('Listado Clientes')
            var.cv.setAuthor('Diego Lago Paz')

            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=12)
            textotitulo = 'LISTADO CLIENTES'

            Informes.cabecera(self)
            Informes.pie(textotitulo)
            var.cv.drawString(255, 690, textotitulo)
            var.cv.line(40, 685, 530, 685)

            items = ['DNI', 'Nombre', 'Formas de Pago']
            var.cv.drawString(65, 675, items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(400, 675, items[2])
            var.cv.line(40, 670, 530, 670)

            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, pagos from clientes order by apellidos, nombre')
            var.cv.setFont('Helvetica', size=8)

            if query.exec_():
                print("query")
                i = 50
                j = 655
                while query.next():

                    if j <= 80:
                        var.cv.drawString(460, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de Pago']
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(400, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawString(i, j, str(query.value(0)))
                    var.cv.drawString(i + 140, j, str(query.value(1) + ', ' + query.value(2)))
                    var.cv.drawString(i + 310, j, str(query.value(3)))
                    j = j - 20
            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('clientes.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error en informes clientes, ', error)

    def cabecera(self):
        try:
            logo = '.\\img\logo-empresa.jpg'
            var.cv.line(40, 800, 530, 800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50, 785, 'Import-Export Vigo')
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50, 770, 'CIF: A0000000H')
            var.cv.drawString(50, 755, 'Dirección: Avenida Galicia,101')
            var.cv.drawString(50, 740, 'Vigo - 36216 - Spain')
            var.cv.drawString(50, 725, 'e-mail: micorreo@mail.com')
            var.cv.drawImage(logo, 425, 735)
            var.cv.line(40, 710, 530, 710)
        except Exception as error:
            print('Error en cabecera informe', error)

    def pie(self, texto):
        try:
            var.cv.line(50, 50, 530, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y  %H.%M.%S')
            var.cv.setFont('Helvetica', size=6)
            var.cv.drawString(70, 40, str(fecha))
            var.cv.drawString(255, 40, str(texto))
            var.cv.drawString(500, 40, str('Página %s ' % var.cv.getPageNumber()))
        except Exception as error:
            print('Error creación de pie de informe clientes', error)

    def listadoProductos(self):
        try:
            var.cv = canvas.Canvas('informes/listadoproductos.pdf')
            var.cv.setTitle('Listado Artículos')
            var.cv.setAuthor('Departamento de Administración')

            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=12)
            textotitulo = 'LISTADO ARTÍCULOS'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            var.cv.drawString(255, 690, textotitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['Código', 'Artículo', 'Precio/Kg']
            var.cv.drawString(60, 675, items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(430, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, producto, precio from productos order by'
                          ' producto')
            var.cv.setFont('Helvetica', size=8)
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(460, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textotitulo)
                        var.cv.drawString(255, 690, textotitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['Código', 'Artículo', 'Precio/Kg']
                        var.cv.drawRightString(60, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(430, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655
                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawRightString(i + 20, j, str(query.value(0)))
                    var.cv.drawString(i + 140, j, str(query.value(1)))
                    var.cv.drawString(i + 380, j, str(query.value(2)))
                    j = j - 20
            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('productos.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error en informes productos, ', error)
