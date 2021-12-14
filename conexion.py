from datetime import datetime

import xlwt as xlwt
from PyQt5 import QtSql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import xlrd
from img import var
import clients


class Conexion():
    def db_connect(filename):
        try:
            db=QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filename)
            if not db.open():
                QtWidgets.QMessageBox.critical(None,'Error al abrir la bbdd',QtWidgets.QMessageBox.Cancel)
                return False
            else :
                print('conexion establecida')
                return True
        except Exception as error:
            print('Error en conexion con bbdd', error)
    '''
    Gestion BBDD articulo
    '''
    def altaArt(newArt):
        if var.ui.lblid.text()== "":
            try:
                query = QtSql.QSqlQuery()
                query.prepare('insert into articulos (nombre, precio) VALUES (:nombre, :precio)')
                query.bindValue(':nombre', str(newArt[0]).lower())
                query.bindValue(':precio', newArt[1])
                if query.exec_():
                    print('Inserción correcta')
                    popup = QtWidgets.QMessageBox()
                    popup.setWindowTitle('Aviso')
                    popup.setText('Articulo dado de alta')
                    popup.setIcon(QtWidgets.QMessageBox.Information)
                    popup.exec()
                else:
                    print('Error:', query.lastError().text())
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Aviso")
                    msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                    msgBox.setText("El articulo no ha sido guardado en la BD")
                    msgBox.exec()
            except Exception as error:
                print('Problemas alta articulo', error)
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("Error al guardar el articulo en la BD")
                msgBox.exec()
        else:
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle('Aviso')
            popup.setText('Estás trabajando con un artículo seleccionado. \nPara guardar un nuevo artículo deselecciona el \n actual pulsando el boton "resetear"')
            popup.setIcon(QtWidgets.QMessageBox.Information)
            popup.exec()

    def cargarTabArt():
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos order by nombre')
            if query.exec_():
                while query.next():
                    codigo = str(query.value(0))
                    nombre = query.value(1)
                    nombre = nombre.lower()
                    precio = query.value(2)
                    var.ui.tabArticulos.setRowCount(index + 1) #creamos la fila y luego cargamos datos
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio + "€"))
                    index += 1
        except Exception as error:
            print('Problemas mostrar tabla articulos', error)

    def bajaArt():
        codigo = var.ui.lblid.text()
        try:
            query=QtSql.QSqlQuery()
            query.prepare('delete from articulos where codigo = :codigo')
            query.bindValue(':codigo',str(codigo))

            if query.exec_():
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle('Aviso')
                popup.setText('Articulo dado de baja')
                popup.setIcon(QtWidgets.QMessageBox.Information)
                popup.exec()
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("El articulo no ha sido dado de baja en la BD")
                msgBox.exec()
            Conexion.cargarTabArt()
        except Exception as error:
            print('Error en bajaArt', error)

    def modifArt():
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update articulos set nombre=:nombre, precio=:precio where codigo = :codigo')
            query.bindValue(':nombre', var.ui.txtNombreArticulo.text().lower())
            query.bindValue(':precio', var.ui.txtPrecioArticulo.text())
            query.bindValue(':codigo', var.ui.lblid.text())
            print(var.ui.lblid.text())
            if query.exec_():
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle('Aviso')
                popup.setText('Articulo modificado')
                popup.setIcon(QtWidgets.QMessageBox.Information)
                popup.exec()
            else:
                print('Error al ejecutar query:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("Error al modificar el articulo")
                msgBox.exec()
            Conexion.cargarTabCli()
            Conexion.cargarTabArt()
        except Exception as error: print("Error en modulo modifart", error)

    def buscarArt():
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from articulos where nombre = :nombre')
            query.bindValue(':nombre', var.ui.txtNombreArticulo.text())
            if query.exec_():
                print("funciona")
                while query.next():
                    codigo = str(query.value(0))
                    nombre = query.value(1)
                    nombre = nombre.lower()
                    precio = query.value(2)
                    var.ui.tabArticulos.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tabArticulos.setItem(index, 0, QtWidgets.QTableWidgetItem(codigo))
                    var.ui.tabArticulos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabArticulos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio + "€"))
                    index += 1
        except Exception as error:
            print('Problemas mostrar tabla busqueda articulos', error)
    '''
    Gestion BBDD cliente
    '''
    def altaCli(newCli):
        try:
            print(newCli)
            query = QtSql.QSqlQuery()
            query.prepare('insert into clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pagos )'
                          'VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pagos)')
            query.bindValue(':dni', str(newCli[0]))
            query.bindValue(':alta', str(newCli[1]))
            query.bindValue(':apellidos', str(newCli[3]))
            query.bindValue(':nombre', str(newCli[2]))
            query.bindValue(':direccion', str(newCli[4]))
            query.bindValue(':provincia', str(newCli[5]))
            query.bindValue(':municipio', str(newCli[6]))
            query.bindValue(':sexo', str(newCli[7]))
            query.bindValue(':pagos', str(newCli[8]))
            if query.exec_():
                print('Inserción correcta')
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle('Aviso')
                popup.setText('Cliente dado de alta')
                popup.setIcon(QtWidgets.QMessageBox.Information)
                popup.exec()
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("El cliente no ha sido guardado en la BD")
                msgBox.exec()
        except Exception as error:
            print('Problemas alta cliente', error)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setIcon((QtWidgets.QMessageBox.Warning))
            msgBox.setText("Error al guardar cliente  en la BD")
            msgBox.exec()

    def oneCli(dni):
        try:
            record=[]
            query=QtSql.QSqlQuery()
            query.prepare('select direccion, provincia,municipio,sexo from clientes where dni=:dni')
            query.bindValue(':dni',dni)
            if query.exec_():
                while query.next():
                    for i in range(4):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas al devolver el cliente marcado', error)

    def bajaCli():
        dni = var.ui.txtDNI.text()
        try:
            query=QtSql.QSqlQuery()
            query.prepare('delete from clientes where dni = :dni')
            print(dni)
            query.bindValue(':dni',str(dni))

            if query.exec_():
                print("funcina")
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle('Aviso')
                popup.setText('Cliente dado de baja')
                popup.setIcon(QtWidgets.QMessageBox.Information)
                popup.exec()
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("El cliente no ha sido dado de baja en la BD")
                msgBox.exec()
            Conexion.cargarTabCli()
        except Exception as error:
            print('Error en bajaCli', error)

    def cargarTabCli():
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, alta, pagos from clientes order by apellidos')
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(2)
                    nombre = query.value(1)
                    alta = query.value(3)
                    pago = query.value(4)
                    var.ui.tabClientes.setRowCount(index + 1) #creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index += 1
        except Exception as error:
            print('Problemas mostrar tabla clientes', error)

    def modifCli(modcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set alta=:alta, apellidos=:apellidos, nombre=:nombre, direccion=:direccion, provincia=:provincia, municipio=:municipio, sexo=:sexo, pagos=:pagos where dni = :dni')
            query.bindValue(':dni', str(modcliente[0]))
            query.bindValue(':alta', str(modcliente[1]))
            query.bindValue(':apellidos', str(modcliente[2]))
            query.bindValue(':nombre', str(modcliente[3]))
            query.bindValue(':direccion', str(modcliente[4]))
            query.bindValue(':provincia', str(modcliente[5]))
            query.bindValue(':municipio', str(modcliente[6]))
            query.bindValue(':sexo', str(modcliente[7]))
            query.bindValue(':pagos', str(modcliente[8]))
            if query.exec_():
                print("funciona")
                popup = QtWidgets.QMessageBox()
                popup.setWindowTitle('Aviso')
                popup.setText('Cliente modificado')
                popup.setIcon(QtWidgets.QMessageBox.Information)
                popup.exec()
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("Error al modificar el cliente")
                msgBox.exec()
            Conexion.cargarTabCli()
        except Exception as error: print("Error en modulo modifcli", error)

    def cargaProv(self):
        try:
            prov = [""]
            ids = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id,provincia FROM provincias')
            if query.exec_():
                while query.next():
                    id = query.value(0)
                    ids.append(id)
                    provin = query.value(1)
                    prov.append(provin)
                clients.Clientes.cargaProv(prov)
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("El cliente no ha sido cargado")
                msgBox.exec()
        except Exception as error:
            print('Problemas cargar provincias', error)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setIcon((QtWidgets.QMessageBox.Warning))
            msgBox.setText("Error al cargar provincias de la BD")
            msgBox.exec()

    def CargaMun(prov):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                'SELECT id FROM provincias WHERE provincia=:pro')
            query.bindValue(':pro', prov)
            if query.exec_():
                while query.next():
                    idp = query.value(0)
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("La provincia no ha sido cargada")
                msgBox.exec()
            mun = [""]
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id,municipio FROM municipios WHERE provincia_id=:idp')
            query.bindValue(':idp', idp)
            if query.exec_():
                while query.next():
                    munic = query.value(1)
                    mun.append(munic)
                clients.Clientes.cargaMun(mun)
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("El cliente no ha sido cargado")
                msgBox.exec()
        except Exception as error:
            print('Problemas cargar provincias', error)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setIcon((QtWidgets.QMessageBox.Warning))
            msgBox.setText("Error al cargar provincias de la BD")
            msgBox.exec()

    def cargarExcel():
        try:
            book = xlrd.open_workbook("img/DATOSCLIENTES.xls")
            sheet = book.sheet_by_name("Folla1")
            for r in range(1, sheet.nrows):
                dni = sheet.cell(r,0).value
                alta = municipio = sheet.cell(r,1).value
                apellidos = sheet.cell(r,2).value
                nombre = sheet.cell(r,3).value
                direccion = sheet.cell(r,4).value
                provincia = sheet.cell(r,5).value
                municipio = sheet.cell(r,6).value
                sexo = sheet.cell(r,7).value
                pagos = sheet.cell(r,8).value
                newCli=[dni,alta, nombre, apellidos, direccion, provincia,municipio, sexo, pagos]
                if(clients.Clientes.validarDNI(newCli[0])):
                    conexion.Conexion.altaCli(newCli)
        except Exception as error:
            print('Error en cargarExcel', error)

    def ExportarExcel(self):
        try:
            conexion.Conexion.exportExcel(self)
            try:
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Datos exportados con éxito.")
                msgBox.setWindowTitle("Operación completada")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje generado exportar datos ', error)
        except Exception as error:
            print('Error en evento exportar datos ',error)

    def exportExcel(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls', options=option)
            wb = xlwt.Workbook()
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'APELIDOS')
            sheet1.write(0, 2, 'NOME')
            sheet1.write(0, 3, 'DIRECCION')
            sheet1.write(0, 4, 'PROVINCIA')
            sheet1.write(0, 5, 'SEXO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_():
                while query.next():
                    sheet1.write(f, 0, query.value(0))
                    sheet1.write(f, 1, query.value(2))
                    sheet1.write(f, 2, query.value(3))
                    sheet1.write(f, 3, query.value(4))
                    sheet1.write(f, 4, query.value(5))
                    sheet1.write(f, 5, query.value(7))
                    f+=1
            wb.save(directorio)

        except Exception as error:
            print('Error en conexion para exportar excel ',error)