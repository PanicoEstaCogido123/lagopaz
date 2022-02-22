#Variables de ventana

from main import FileDialogAbrir
from window import Ui_MainWindow
from windowcal import Ui_windowcal

global ui, dlgaviso, dlgcalendar, dlgabrir, copia, msg, cv, btnfacdel, cmbProducto, txtCantidad, precio, codpro
filedb='bbdd.db'
ui: Ui_MainWindow
#dlgaviso: DialogoAviso
dlgCalendar: Ui_windowcal
dlgAbrir: FileDialogAbrir

'''
otras variables
'''
from img import abrirCarpeta
from img import bajar
from img import calendario
from img import imprimir
from img import limpiar
from img import salir
from img import subir