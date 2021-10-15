import clients
from window import *
from windowaviso import *
from windowcal import *
from datetime import *
import sys, var, events

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso,self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        #Correcion del error al exportar la ventana
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
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
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
        Eventos combobox
        '''
        clients.Clientes.cargaProv(self)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.cmbMun.activated[str].connect(clients.Clientes.selMun)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())