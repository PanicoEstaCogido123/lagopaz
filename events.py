import os.path, sys, var, shutil, zipfile

import conexion
from window import*
from datetime import date, datetime
from PyQt5 import  QtPrintSupport

class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print('Error en módulo salir ',error)

    def abrircal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error en el modulo abrircal ',error)

    def resizeTablaCli(self):
        header = var.ui.tabClientes.horizontalHeader()
        for i in range(5):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
            if i == 0 or i==3:
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

    def Abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print('Error al abrir el cuadro de dialogo ', error)

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = str((fecha)+'_backup.zip')
            option = QtWidgets.QFileDialog.Option()
            directorio, filename=var.dlgabrir.getSaveFileName(None,'Guardar Copia', var.copia,'.zip',options=option)
            if var.dlgabrir.Accepted and filename != '':
                fichzip=zipfile.ZipFile(var.copia,'w')
                fichzip.write(var.filedb,os.path.basename(var.filedb),zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia),str(directorio))
        except Exception as error:
            print('Error en crearBackup', error)

    def restaurarBackup(self):
        try:
            option = QtWidgets.QFileDialog.Option()
            filename = var.dlgabrir.getOpenFileName(None,"Restaurar Copia de Seguridade","","*zip",options=option)
            if var.dlgabrir.Accepted and filename != "":
                file=filename[0]
                print(file)
                with zipfile.ZipFile(str(file),"r")as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTabCli()
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Copia de seguridad restaurada")
            msg.exec()
        except Exception as error:
            print('Error en restaurarBackup', error)

    def imprimir(self):
        try:
            printDialog =QtPrintSupport.QPrintDialog()
            if printDialog.exec_():
                printDialog.show()
            print("impresion")
        except Exception as error:
            print('Error en imprimir', error)