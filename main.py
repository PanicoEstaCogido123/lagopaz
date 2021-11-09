import locale

import clients
import conexion
from window import *
from windowaviso import *
from windowcal import *
from datetime import *
import sys,var,events,locale
locale.setlocale(locale.LC_ALL,'es-ES')

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnBoxAviso.accepted.connect(self.accepted)
        var.dlgaviso.btnBoxAviso.rejected.connect(self.reject)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''
        Ventana calendario
        '''
        super(DialogCalendar, self).__init__()
        var.dlgcalendar=Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual=datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendar.calendarWidget.clicked.connect(clients.Clientes.cargarFecha)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de boton
        '''
        var.ui.btnLimpiaFormCliente.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
        var.ui.btnBorraCli.clicked.connect(conexion.Conexion.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        '''
        Eventos de menus
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.letraCapital)

        '''
        Eventos QtabWidgets
        '''
        events.Eventos.resizeTablaCli(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCLi)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        conexion.Conexion.db_connect((var.filedb))
        conexion.Conexion.cargarTabCli()
        '''
        Eventos combobox
        '''
        clients.Clientes.cargaProv(self)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)

        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha_2,1)
        day=datetime.now()
        var.ui.lblFecha_2.setText(day.strftime('%A, %d de %B de %Y').capitalize())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())