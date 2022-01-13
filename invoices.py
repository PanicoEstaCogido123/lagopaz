from PyQt5 import QtSql, QtWidgets

import conexion
from img import var


class Invoices():
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
        except Exception as error: print("Error en modulo factura", error)
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
        except Exception as error: print("Error en modulo cargaClienteFactura", error)

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
        except Exception as error: print("Error en modulo buscarClienteFactura", error)

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
                        fechafac = query.value(2)
                var.ui.lblClienteNumFactura.setText(codfac)
                var.ui.txtDniFactura.setText(dni)
                var.ui.txtFechaFactura.setText(fechafac)
                Invoices.buscarClienteFactura(self)
        except Exception as error:
            print("Error en modulo cargaClienteFactura", error)

    def cargarLineaVenta(self):
        try:
            print("dentro")
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            var.txtCantidad = QtWidgets.QLineEdit()
            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3,var.txtCantidad)
        except Exception as error:
            print("Error en modulo cargarLineaVenta", error)