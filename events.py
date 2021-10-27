'''

Fichero de eventos generales

'''
import sys,var
from window import*

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