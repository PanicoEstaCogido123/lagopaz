from PyQt5 import QtSql
from PyQt5 import QtWidgets

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