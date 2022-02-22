import locale

from PyQt5 import QtSql, QtWidgets, QtCore

import conexion
from img import var


class Invoices:
    def facturar():
        try:
            dni = var.ui.txtDniFactura.text()
            data = var.ui.txtFechaFactura.text()
            articulo = [dni, data]

            query = QtSql.QSqlQuery()
            query.prepare('insert into facturas (dni, fechafac) VALUES (:dni, :fechafac)')
            query.bindValue(':dni', str(articulo[0]).lower())
            query.bindValue(':fechafac', articulo[1])
            if query.exec_():
                print('Inserción correcta')
                conexion.Conexion.cargaTabFactura()
            codfac = conexion.Conexion.buscaCodFac()
            var.ui.lblClienteNumFactura.setText(str(codfac))
        except Exception as error:
            print("Error en modulo facturar", error)

    def procesoVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo = var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodigoPrecio(articulo)
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.codpro = dato[0]
            var.precio = dato[1].replace(",", ".")
        except Exception as error:
            print("Error en modulo procesoVenta", error)

    def totalLineaVenta(self=None):
        try:
            venta = []
            row = var.ui.tabVentas.currentRow()
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')), 2)
            totalLinea = round(float(var.precio) * float(cantidad), 2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(totalLinea) + '€'))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)
            codfac = var.ui.lblClienteNumFactura.text()
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append(float(var.precio))
            venta.append(float(cantidad))
            conexion.Conexion.cargarVentas(venta)

        except Exception as error:
            print("Error en modulo totalLineaVenta", error)

    def cargaClienteFactura(self):
        try:
            fila = var.ui.tabClientes.selectedItems()
            if fila:
                row = [dato.text() for dato in fila]
                dni = row[0]
                query = QtSql.QSqlQuery()
                query.prepare('SELECT nombre, apellidos FROM clientes WHERE dni="' + dni + '"')
                if query.exec_():
                    while query.next():
                        nombre = query.value(0)
                        apellidos = query.value(1)
                        nombreCompleto = str(nombre) + " " + str(apellidos)
                var.ui.txtDniFactura.setText(dni)
                var.ui.lblClienteFactura.setText(nombreCompleto)
        except Exception as error:
            print("Error en modulo cargaClienteFactura", error)

    def buscarClienteFactura(self):
        try:
            dni = var.ui.txtDniFactura.text()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT nombre, apellidos FROM clientes WHERE dni="' + dni + '"')
            if query.exec_():
                while query.next():
                    nombre = query.value(0)
                    apellidos = query.value(1)
                    nombreCompleto = str(nombre) + " " + str(apellidos)
                var.ui.lblClienteFactura.setText(nombreCompleto)
        except Exception as error:
            print("Error en modulo buscarClienteFactura", error)

    def cargarFactura(self):
        try:
            fila = var.ui.tabClientesFacturas.selectedItems()
            if fila:
                row = [dato.text() for dato in fila]
                codigo = row[0]
                query = QtSql.QSqlQuery()
                query.prepare('SELECT codfac, dni, fechafac FROM facturas WHERE codfac="' + codigo + '"')
                if query.exec_():
                    while query.next():
                        codfac = query.value(0)
                        codfac = str(codfac)
                        dni = query.value(1)
                        dni = dni.upper()
                        fechafac = query.value(2)
                var.ui.lblClienteNumFactura.setText(codfac)
                var.ui.txtDniFactura.setText(dni)
                var.ui.txtFechaFactura.setText(fechafac)
                Invoices.buscarClienteFactura(self)
                conexion.Conexion.cargarLineasVenta(str(var.ui.lblClienteNumFactura.text()))
        except Exception as error:
            print("Error en modulo cargaClienteFactura", error)

    def cargarLineaVenta(index):
        try:
            var.cmbProducto = QtWidgets.QComboBox()
            conexion.Conexion.cargarCmbProducto()

            # var.txtCantidad = QtWidgets.QLineEdit()

            var.ui.tabVentas.setRowCount(index + 1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)
        except Exception as error:
            print("Error en modulo cargarLineaVenta", error)
