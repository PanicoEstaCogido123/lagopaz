from PyQt5 import QtSql
from PyQt5 import QtWidgets
import var

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
                    var.ui.tabClientes.setRowCount(index+1) #creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index += 1
        except Exception as error:
            print('Problemas mostrar tabla clientes', error)

    def cargaProv(self):
        try:
            print("dentro")
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            if query.exec_():
                print("ejecutado")
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))

        except Exception as error: print("Error en modulo cargaProv", error)
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