import xlwt as xlwt, sqlite3, csv, os.path, xlrd
from PyQt5 import QtSql
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

import invoices
from img import var
import clients

class Conexion():
    def create_DB(filename):
        """

        Modulo que se ejecuta al principio del programa.
        Crea las tablas y carga municipios y provincias.
        Crea los directorios necesarios.
        :param filename:
        :rtype object:

        """
        try:
            con=sqlite3.connect(database=filename)
            cur=con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS clientes (dni TEXT NOT NULL, alta TEXT, apellidos TEXT NOT NULL, '
                        'nombre TEXT, direccion TEXT, provincia TEXT, municipio TEXT, sexo TEXT, pagos TEXT, '
                        'PRIMARY KEY(dni))')
            cur.execute('CREATE TABLE IF NOT EXISTS articulos (codigo INTEGER, nombre TEXT NOT NULL, precio TEXT, '
                        'PRIMARY KEY(codigo AUTOINCREMENT))')
            cur.execute('CREATE TABLE IF NOT EXISTS facturas (codfac INTEGER NOT NULL, dni TEXT NOT NULL, fechafac TEXT NOT NULL, '
                        'PRIMARY KEY(codfac AUTOINCREMENT), FOREIGN KEY(dni) REFERENCES clientes(dni))')

            cur.execute('CREATE TABLE IF NOT EXISTS municipios (provincia_id INTEGER NOT NULL, municipio TEXT NOT NULL, '
                        'id INTEGER NOT NULL, PRIMARY KEY(id))')
            cur.execute('CREATE TABLE IF NOT EXISTS provincias (id INTEGER NOT NULL, provincia TEXT NOT NULL, '
                        'PRIMARY KEY(id))')

            cur.execute('CREATE TABLE IF NOT EXISTS ventas ( codventa INTEGER NOT NULL, codfac INTEGER NOT NULL, '
                        'codpro INTEGER NOT NULL, cantidad REAL NOT NULL, PRIMARY KEY(codventa AUTOINCREMENT), '
                        'FOREIGN KEY(codpro) REFERENCES articulos(codigo), '
                        'FOREIGN KEY(codfac) REFERENCES facturas(codfac))')
            con.commit()

            con.execute('select count() from provincias')
            numero = cur.fetchone()[0]
            if int(numero) == 0:
                with open('provincias.csv', 'r', encoding="utf-8") as fin:
                    dr = csv.DictReader(fin)
                    to_db = [(i['id'], i['provincia'])for i in dr]
                cur.executemany('insert into provincias (id, provincia) VALUES (?, ?);', to_db)
                con.commit()
            con.close()

            if not os.path.exists('.\\informes'):
                os.mkdir('.\\informes')
        except Exception as error:
            print("Error en create_DB ", error)

    def db_connect(filename):
        """

        Realiza la conexión a la bbdd
        :param filename:
        :return: True si es correcto, False si no
        :rtype: Booleano

        """
        try:
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName(filename)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'Error al abrir la bbdd', QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print('conexion establecida')
                return True
        except Exception as error:
            print('Error en conexion con bbdd', error)
    '''
    Productos
    '''
    def bajaFact():
        """

        bajaFact

        """
        try:
            numfac = var.ui.lblClienteNumFactura.text()
            query = QtSql.QSqlQuery()
            query.prepare('delete from facturas where codfac = :codfac')
            query.bindValue(':codfac', int(numfac))
            if query.exec_():
                Conexion.cargaTabFactura()
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("La factura ha sido dada de baja")
                msgBox.setWindowTitle("Aviso")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                Conexion.delVentaFac(numfac)
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("La factura no ha sido dada de baja. Recuerda seleccionarla antes de eliminarla")
                msgBox.exec()

        except Exception as error:
            print('Error en dar baja factura', error)

    def delVentaFac(numfac):
        """

        delVentaFac
        :param numfac:

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(numfac))
            if query.exec_():
                Conexion.cargaTabFactura()
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Las ventas han sido dadas de baja")
                msgBox.setWindowTitle("Aviso")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                print('Error:', query.lastError().text())
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Aviso")
                msgBox.setIcon((QtWidgets.QMessageBox.Warning))
                msgBox.setText("La factura no ha sido dada de baja. Recuerda seleccionarla antes de eliminarla")
                msgBox.exec()
        except Exception as error:
            print("error en delVentaFac en Conexion", error)

    def obtenerCodigoPrecio(articulo):
        """

        obtenerCodigoPrecio
        :param articulo:
        :return: Array

        """
        try:
            datos=[]
            query=QtSql.QSqlQuery()
            query.prepare('select codigo, precio from articulos where nombre=:articulo')
            query.bindValue(':articulo',str(articulo))
            if query.exec_():
                while query.next():
                    datos.append(int(query.value(0)))
                    datos.append(str(query.value(1)))
                    return datos
        except Exception as error:
            print("error en obtenerCodigoPrecio en Conexion", error)

    def cargarVentas(venta):
        """

        cargarVentas
        :param venta:

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('insert into ventas (codfac, codpro, precio, cantidad) values (:codfac,:codpro, :precio, :cantidad)')
            query.bindValue(':codfac', int(venta[0]))
            query.bindValue(':codpro', int(venta[1]))
            query.bindValue(':precio', int(venta[2]))
            query.bindValue(':cantidad', int(venta[3]))
            if query.exec_():
                var.ui.lblVentas.setText("Realizada")
            else:
                var.ui.lblVentas.setStyleSheet("QLabel{color:red;}")
                var.ui.lblVentas.setText("Error en venta")
        except Exception as error:
            print("error en cargarVentas ", error)

    def buscaCodFac():
        """

        :return: int
        buscaCodFac

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select codfac from facturas order by codfac desc limit 1')
            if query.exec_():
                while query.next():
                    dato = query.value(0)
            return dato
        except Exception as error:
            print("error en buscaCodFac ", error)

    def cargarCmbProducto():
        """

        cargarCmbProducto

        """
        try:
            var.cmbProducto.clear()
            query = QtSql.QSqlQuery()
            var.cmbProducto.addItem('')#ponemos la primera línea en blanco
            query.prepare(('select nombre from articulos order by nombre'))
            if query.exec_():
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))
        except Exception as error:
            print("error en cargarCmbProducto ", error)

    def altaFactura(newFactura):
        """

        altaFactura
        :param newFactura:

        """
        pass

    def cargaTabFactura():
        """

        cargaTabFactura

        """
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('select codfac, dni, fechafac from facturas order by codfac')
            if query.exec_():
                while query.next():
                    codfac = str(query.value(0))
                    dni = query.value(1)
                    fechafac = query.value(2)

                    var.btnfacdel = QtWidgets.QPushButton()
                    icopapelera = QtGui.QPixmap("img/salir.png")
                    var.btnfacdel.setFixedSize(24, 24)
                    var.btnfacdel.setIcon(QtGui.QIcon(icopapelera))


                    var.ui.tabClientesFacturas.setRowCount(index + 1) #creamos la fila y luego cargamos datos
                    var.ui.tabClientesFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(codfac))
                    #var.ui.tabClientesFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientesFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFact)
                    lay_out.setAlignment(QtCore.Qt.AlignVCenter)
                    var.ui.tabClientesFacturas.setCellWidget(index, 2, cell_widget)
                    index += 1
        except Exception as error:
            print('Problemas mostrar tabla facturas', error)
        pass

    def altaArt(newArt):
        """

        altaArt
        :param newArt:

        """
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
        """

        cargarTabArt

        """
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
        """

        bajaArt

        """
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
        """

        modifArt

        """
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
        """

        buscarArt

        """
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

    def altaCli(newCli):
        """

        altaCli
        :param newCli:

        """
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
        """

        oneCli
        :param dni:
        :return: array

        """
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
        """

        bajaCli

        """
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
        """

        cargarTabCli

        """
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
        """

        modifCli
        :param modcliente:

        """
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
        """

        cargaProv

        """
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
        """

        CargaMun
        :param prov:

        """
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
        """

        cargarExcel

        """
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
        """

        ExportarExcel

        """
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
        """

        exportExcel

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls', options=option)
            wb = xlwt.Workbook()
            #add_sheet is used to create sheet.
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

    def cargarLineasVenta(codfac):
        """

        cargarLineasVenta
        :param prov:

        """
        try:
            #Limpiar la tabla
            var.ui.tabVentas.clearContents()
            #Declaracion de atributos
            suma = 0.0
            index = 0
            #Query para buscar los datos de las ventas
            query = QtSql.QSqlQuery()
            query.prepare('select codventa, codpro, cantidad, precio from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            #Cargar líneas productos
            if query.exec_():
                while query.next():
                    #Asignación de los valores para la línea del artículo
                    codventa = query.value(0)
                    codpro = query.value(1)
                    cantidad = query.value(2)
                    precio = query.value(3)
                    totalVenta = cantidad * precio
                    #Query para buscar el nombre del artículo
                    subquery = QtSql.QSqlQuery()
                    subquery.prepare('select nombre from articulos where codigo = :codpro')
                    subquery.bindValue(':codpro', int(codpro))
                    if subquery.exec_():
                        while subquery.next():
                            nombreArticulo = subquery.value(0)
                            print(nombreArticulo)
                    #Meter los datos en una nueva línea de producto
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codventa)))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(nombreArticulo)))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(precio)))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(cantidad)))
                    var.ui.tabVentas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(totalVenta)))
                    index = index + 1
                #Crear línea para agregar una nueva venta a la factura
                #Creación de los widgets para la línea
                var.txtCantidad= QtWidgets.QLineEdit()
                var.cmbProducto = QtWidgets.QComboBox()
                #Evento para cargar el precio
                var.cmbProducto.currentIndexChanged.connect(invoices.Invoices.procesoVenta)
                #Cargar los valores del combo
                Conexion.cargarCmbProducto()
                #Creación de la línea
                var.ui.tabVentas.setRowCount(index + 1)
                var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
                var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
                var.txtCantidad.returnPressed.connect(invoices.Invoices.totalLineaVenta)
                invoices.Invoices.cargarFactura()
                invoices.Invoices.cargarLineaVenta(index)
                Conexion.cargarLineasVenta()
                var.ui.tabVentas.scrollToBottom()
        except Exception as error:
            print('error cargar las lineas de factura', error)