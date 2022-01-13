import articles
import sys, events, locale, informes

import invoices
from img import var
import conexion
import clients
from window import *
from windowaviso import *
from windowcal import *
from datetime import *
locale.setlocale(locale.LC_ALL,'es-ES')

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir,self).__init__()

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar=Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual=datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.calendarWidget.clicked.connect(clients.Clientes.cargarFecha)

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnBoxAviso.accepted.connect(self.accepted)
        var.dlgaviso.btnBoxAviso.rejected.connect(self.reject)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de boton
        '''
        var.ui.btnFacturar.clicked.connect(invoices.Invoices.facturar)
        var.ui.btnBuscarFactura.clicked.connect(invoices.Invoices.buscarClienteFactura)
        var.ui.btnLimpiaFormCliente.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
        var.ui.btnCalendarFactura.clicked.connect(events.Eventos.abrircal)
        var.ui.btnBorraCli.clicked.connect(conexion.Conexion.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnGuardarArticulo.clicked.connect(articles.Articles.guardaArticulo)
        var.ui.btnModificarArticulo.clicked.connect(conexion.Conexion.modifArt)
        var.ui.btnBorrarArticulo.clicked.connect(conexion.Conexion.bajaArt)
        var.ui.btnBuscarArticulo.clicked.connect(conexion.Conexion.buscarArt)
        var.ui.btnLimpiaFormArticulo.clicked.connect(articles.Articles.limpiaFormArt)
        '''
        Eventos de barra de menus y herramientas
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.Abrir)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRestaurar_BBDD.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionImportar_Datos.triggered.connect(conexion.Conexion.cargarExcel)
        var.ui.actionExportar_Datos.triggered.connect(conexion.Conexion.ExportarExcel)
        var.ui.actionbarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionbarAbrirCarpeta.triggered.connect(events.Eventos.Abrir)
        var.ui.actionbarCrearBackup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionbarRestaurarBackup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionbarImprimir.triggered.connect(events.Eventos.imprimir)
        var.ui.actionListado_Clientes.triggered.connect(informes.Informes.listadoClientes)
        '''
        Eventos caja de texto DNI
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtApel.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.sBoxEnvio.valueChanged.connect(clients.Clientes.actualizarEnvio)
        '''
        Eventos QtabWidgets
        '''
        var.ui.tabClientesFacturas.clicked.connect(invoices.Invoices.cargarFactura)
        events.Eventos.resizeTablaCli(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.clicked.connect(invoices.Invoices.cargaClienteFactura)
        var.ui.tabArticulos.clicked.connect(articles.Articles.cargaArticulo)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabArticulos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabClientesFacturas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabVentas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        #invoices.Invoices.preparaTabFac(self)
        invoices.Invoices.cargarLineaVenta(self)
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargarTabCli()
        conexion.Conexion.cargarTabArt()
        conexion.Conexion.cargaProv(self)
        conexion.Conexion.cargaTabFactura()
        '''
        Eventos combobox
        '''
        var.ui.cmbProv.activated[str].connect(conexion.Conexion.CargaMun)
        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha_2, 1)
        day=datetime.now()
        var.ui.lblFecha_2.setText(day.strftime('%A, %d de %B de %Y').capitalize())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir=FileDialogAbrir()
    window.show()
    sys.exit(app.exec())