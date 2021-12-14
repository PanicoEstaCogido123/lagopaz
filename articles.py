from img import var
import conexion
from window import *
from PyQt5 import QtSql

class Articles():
    def guardaArticulo(self):
        if (var.ui.txtNombreArticulo.text()!= ""):
            try:
                nombre = var.ui.txtNombreArticulo.text()
                precio = var.ui.txtPrecioArticulo.text()
                articulo = [nombre,precio]
                conexion.Conexion.altaArt(articulo)
                conexion.Conexion.cargarTabArt()
            except Exception as error:
                print('Error en guardar clientes', error)
        else:
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle('Error')
            popup.setText('Introduzca un nombre para el articulo')
            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.exec()

    def cargaArticulo(self):
        try:
            fila = var.ui.tabArticulos.selectedItems()
            if fila:
                row = [dato.text() for dato in fila]
                codigo = row[0]
                query = QtSql.QSqlQuery()
                query.prepare(
                    'SELECT codigo, nombre, precio FROM articulos WHERE codigo="' + codigo + '"')
                if query.exec_():
                    while query.next():
                        codigo = str(query.value(0))
                        nombre = query.value(1)
                        precio = query.value(2)
                var.ui.lblid.setText(codigo)
                var.ui.txtNombreArticulo.setText(nombre)
                var.ui.txtPrecioArticulo.setText(precio)
        except Exception as error: print("Error en modulo CargaCli",error)

    def limpiaFormArt(self):
        try:
            registros=[var.ui.txtNombreArticulo, var.ui.txtPrecioArticulo, var.ui.lblid]
            for i in registros:
                i.setText('')
        except Exception as error:
            print('Error en limpiar formulario')