# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 735)
        self.tabPrograma = QtWidgets.QWidget(MainWindow)
        self.tabPrograma.setObjectName("tabPrograma")
        self.tabWidget = QtWidgets.QTabWidget(self.tabPrograma)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1011, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.Clientes = QtWidgets.QWidget()
        self.Clientes.setObjectName("Clientes")
        self.lblClientes = QtWidgets.QLabel(self.Clientes)
        self.lblClientes.setGeometry(QtCore.QRect(457, 0, 101, 20))
        self.lblClientes.setObjectName("lblClientes")
        self.tabClientes = QtWidgets.QTableWidget(self.Clientes)
        self.tabClientes.setGeometry(QtCore.QRect(227, 320, 541, 271))
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(5)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabClientes.setHorizontalHeaderItem(4, item)
        self.btnSalir = QtWidgets.QPushButton(self.Clientes)
        self.btnSalir.setGeometry(QtCore.QRect(570, 280, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        self.groupBox = QtWidgets.QGroupBox(self.Clientes)
        self.groupBox.setGeometry(QtCore.QRect(0, 40, 991, 221))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_7.setGeometry(QtCore.QRect(290, 40, 421, 22))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ldlApel = QtWidgets.QLabel(self.layoutWidget_7)
        self.ldlApel.setObjectName("ldlApel")
        self.horizontalLayout_6.addWidget(self.ldlApel)
        self.txtApel = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.txtApel.setText("")
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_6.addWidget(self.txtApel)
        self.label = QtWidgets.QLabel(self.layoutWidget_7)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.txtNome = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout_6.addWidget(self.txtNome)
        self.layoutWidget_8 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_8.setGeometry(QtCore.QRect(290, 130, 421, 19))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.LblSexo = QtWidgets.QLabel(self.layoutWidget_8)
        self.LblSexo.setObjectName("LblSexo")
        self.horizontalLayout_8.addWidget(self.LblSexo)
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget_8)
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.horizontalLayout_8.addWidget(self.rbtFem)
        self.rbtMasc = QtWidgets.QRadioButton(self.layoutWidget_8)
        self.rbtMasc.setObjectName("rbtMasc")
        self.rbtGroupSex.addButton(self.rbtMasc)
        self.horizontalLayout_8.addWidget(self.rbtMasc)
        self.layoutWidget_10 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_10.setGeometry(QtCore.QRect(290, 70, 421, 22))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblDir = QtWidgets.QLabel(self.layoutWidget_10)
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_10.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_10.addWidget(self.txtDir)
        self.layoutWidget_11 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_11.setGeometry(QtCore.QRect(290, 160, 421, 19))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblFormaDePago = QtWidgets.QLabel(self.layoutWidget_11)
        self.lblFormaDePago.setObjectName("lblFormaDePago")
        self.horizontalLayout_11.addWidget(self.lblFormaDePago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.layoutWidget_11)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.chkGroupPago = QtWidgets.QButtonGroup(MainWindow)
        self.chkGroupPago.setObjectName("chkGroupPago")
        self.chkGroupPago.setExclusive(False)
        self.chkGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_11.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget_11)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_11.addWidget(self.chkTarjeta)
        self.chkCargoCuenta = QtWidgets.QCheckBox(self.layoutWidget_11)
        self.chkCargoCuenta.setObjectName("chkCargoCuenta")
        self.chkGroupPago.addButton(self.chkCargoCuenta)
        self.horizontalLayout_11.addWidget(self.chkCargoCuenta)
        self.chkTrans = QtWidgets.QCheckBox(self.layoutWidget_11)
        self.chkTrans.setObjectName("chkTrans")
        self.chkGroupPago.addButton(self.chkTrans)
        self.horizontalLayout_11.addWidget(self.chkTrans)
        self.layoutWidget_12 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_12.setGeometry(QtCore.QRect(290, 100, 421, 22))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblProv = QtWidgets.QLabel(self.layoutWidget_12)
        self.lblProv.setObjectName("lblProv")
        self.horizontalLayout_12.addWidget(self.lblProv)
        self.cmbProv = QtWidgets.QComboBox(self.layoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_12.addWidget(self.cmbProv)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.lblMun = QtWidgets.QLabel(self.layoutWidget_12)
        self.lblMun.setObjectName("lblMun")
        self.horizontalLayout_12.addWidget(self.lblMun)
        self.cmbMun = QtWidgets.QComboBox(self.layoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMun.sizePolicy().hasHeightForWidth())
        self.cmbMun.setSizePolicy(sizePolicy)
        self.cmbMun.setObjectName("cmbMun")
        self.horizontalLayout_12.addWidget(self.cmbMun)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 10, 421, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDNI = QtWidgets.QLabel(self.layoutWidget)
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout.addWidget(self.lblDNI)
        self.txtDNI = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDNI.sizePolicy().hasHeightForWidth())
        self.txtDNI.setSizePolicy(sizePolicy)
        self.txtDNI.setText("")
        self.txtDNI.setObjectName("txtDNI")
        self.horizontalLayout.addWidget(self.txtDNI)
        self.lblValidoDNI = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidoDNI.sizePolicy().hasHeightForWidth())
        self.lblValidoDNI.setSizePolicy(sizePolicy)
        self.lblValidoDNI.setText("")
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        self.horizontalLayout.addWidget(self.lblValidoDNI)
        self.lblFecha = QtWidgets.QLabel(self.layoutWidget)
        self.lblFecha.setObjectName("lblFecha")
        self.horizontalLayout.addWidget(self.lblFecha)
        self.txtFecha = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtFecha.setObjectName("txtFecha")
        self.horizontalLayout.addWidget(self.txtFecha)
        self.btnCalendar = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout.addWidget(self.btnCalendar)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(290, 190, 421, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sBoxEnvio = QtWidgets.QSpinBox(self.widget)
        self.sBoxEnvio.setMaximum(3)
        self.sBoxEnvio.setObjectName("sBoxEnvio")
        self.horizontalLayout_2.addWidget(self.sBoxEnvio)
        self.lblEnvio = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 63, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lblEnvio.setPalette(palette)
        self.lblEnvio.setStyleSheet("QLabel{\n"
"font: 75 8pt \"Hack\";\n"
"color:\'red\';\n"
"\n"
"\n"
"}")
        self.lblEnvio.setObjectName("lblEnvio")
        self.horizontalLayout_2.addWidget(self.lblEnvio)
        self.separadorSuperior = QtWidgets.QFrame(self.Clientes)
        self.separadorSuperior.setGeometry(QtCore.QRect(-3, 20, 1001, 20))
        self.separadorSuperior.setFrameShape(QtWidgets.QFrame.HLine)
        self.separadorSuperior.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separadorSuperior.setObjectName("separadorSuperior")
        self.btnGrabaCli = QtWidgets.QPushButton(self.Clientes)
        self.btnGrabaCli.setGeometry(QtCore.QRect(300, 280, 75, 23))
        self.btnGrabaCli.setObjectName("btnGrabaCli")
        self.SeparadorInferior = QtWidgets.QFrame(self.Clientes)
        self.SeparadorInferior.setGeometry(QtCore.QRect(-3, 260, 1011, 20))
        self.SeparadorInferior.setFrameShape(QtWidgets.QFrame.HLine)
        self.SeparadorInferior.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SeparadorInferior.setObjectName("SeparadorInferior")
        self.btnModifCli = QtWidgets.QPushButton(self.Clientes)
        self.btnModifCli.setGeometry(QtCore.QRect(390, 280, 75, 23))
        self.btnModifCli.setObjectName("btnModifCli")
        self.btnBorraCli = QtWidgets.QPushButton(self.Clientes)
        self.btnBorraCli.setGeometry(QtCore.QRect(480, 280, 75, 23))
        self.btnBorraCli.setObjectName("btnBorraCli")
        self.btnLimpiaFormCliente = QtWidgets.QPushButton(self.Clientes)
        self.btnLimpiaFormCliente.setGeometry(QtCore.QRect(660, 280, 21, 21))
        self.btnLimpiaFormCliente.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/98865.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiaFormCliente.setIcon(icon1)
        self.btnLimpiaFormCliente.setObjectName("btnLimpiaFormCliente")
        self.tabWidget.addTab(self.Clientes, "")
        self.Facturacion = QtWidgets.QWidget()
        self.Facturacion.setObjectName("Facturacion")
        self.label_3 = QtWidgets.QLabel(self.Facturacion)
        self.label_3.setGeometry(QtCore.QRect(470, 290, 61, 21))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.Facturacion, "")
        self.Articulos = QtWidgets.QWidget()
        self.Articulos.setObjectName("Articulos")
        self.label_4 = QtWidgets.QLabel(self.Articulos)
        self.label_4.setGeometry(QtCore.QRect(490, 300, 61, 21))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.Articulos, "")
        self.lblFecha_2 = QtWidgets.QLabel(self.tabPrograma)
        self.lblFecha_2.setGeometry(QtCore.QRect(470, 700, 47, 13))
        self.lblFecha_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFecha_2.setObjectName("lblFecha_2")
        MainWindow.setCentralWidget(self.tabPrograma)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionGuadar = QtWidgets.QAction(MainWindow)
        self.actionGuadar.setObjectName("actionGuadar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionFichero = QtWidgets.QAction(MainWindow)
        self.actionFichero.setObjectName("actionFichero")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionCrear_Backup = QtWidgets.QAction(MainWindow)
        self.actionCrear_Backup.setObjectName("actionCrear_Backup")
        self.actionRestaurar_BBDD = QtWidgets.QAction(MainWindow)
        self.actionRestaurar_BBDD.setObjectName("actionRestaurar_BBDD")
        self.actionbarSalir = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbarSalir.setIcon(icon2)
        self.actionbarSalir.setObjectName("actionbarSalir")
        self.actionbarAbrirCarpeta = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/abrir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbarAbrirCarpeta.setIcon(icon3)
        self.actionbarAbrirCarpeta.setObjectName("actionbarAbrirCarpeta")
        self.actionbarCrearBackup = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/subir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbarCrearBackup.setIcon(icon4)
        self.actionbarCrearBackup.setObjectName("actionbarCrearBackup")
        self.actionbarRestaurarBackup = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/bajar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbarRestaurarBackup.setIcon(icon5)
        self.actionbarRestaurarBackup.setObjectName("actionbarRestaurarBackup")
        self.actionbarImprimir = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/impresora.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbarImprimir.setIcon(icon6)
        self.actionbarImprimir.setObjectName("actionbarImprimir")
        self.actionImportar_Datos = QtWidgets.QAction(MainWindow)
        self.actionImportar_Datos.setObjectName("actionImportar_Datos")
        self.actionExportar_Datos = QtWidgets.QAction(MainWindow)
        self.actionExportar_Datos.setObjectName("actionExportar_Datos")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionImportar_Datos)
        self.menuArchivo.addAction(self.actionExportar_Datos)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHerramientas.addAction(self.actionCrear_Backup)
        self.menuHerramientas.addAction(self.actionRestaurar_BBDD)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.toolBar.addAction(self.actionbarSalir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbarAbrirCarpeta)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbarImprimir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbarCrearBackup)
        self.toolBar.addAction(self.actionbarRestaurarBackup)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblClientes.setText(_translate("MainWindow", "XESTION CLIENTES"))
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI/NIE"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha_Alta"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Formas_Pago"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos Personales"))
        self.ldlApel.setText(_translate("MainWindow", "Apellidos:"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.LblSexo.setText(_translate("MainWindow", "Sexo:"))
        self.rbtFem.setText(_translate("MainWindow", "Mujer"))
        self.rbtMasc.setText(_translate("MainWindow", "Hombre"))
        self.lblDir.setText(_translate("MainWindow", "Direccion:"))
        self.lblFormaDePago.setText(_translate("MainWindow", "Forma de pago:"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkCargoCuenta.setText(_translate("MainWindow", "Cargo en cuenta"))
        self.chkTrans.setText(_translate("MainWindow", "Transferencia"))
        self.lblProv.setText(_translate("MainWindow", "Provincia:"))
        self.lblMun.setText(_translate("MainWindow", "Municipio:"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.lblFecha.setText(_translate("MainWindow", "Fecha Alta:"))
        self.label_2.setText(_translate("MainWindow", "Forma de envío:"))
        self.lblEnvio.setText(_translate("MainWindow", "Recogida por cliente"))
        self.btnGrabaCli.setText(_translate("MainWindow", "Guardar"))
        self.btnModifCli.setText(_translate("MainWindow", "Modificar Cli."))
        self.btnBorraCli.setText(_translate("MainWindow", "Eliminar Cli."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Clientes), _translate("MainWindow", "Clientes"))
        self.label_3.setText(_translate("MainWindow", "En proceso"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Facturacion), _translate("MainWindow", "Facturacion"))
        self.label_4.setText(_translate("MainWindow", "En proceso"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Articulos), _translate("MainWindow", "Articulos"))
        self.lblFecha_2.setText(_translate("MainWindow", "TextLabel"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramientas"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionGuadar.setText(_translate("MainWindow", "Guadar"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como"))
        self.actionFichero.setText(_translate("MainWindow", "Fichero"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionCrear_Backup.setText(_translate("MainWindow", "Crear Backup"))
        self.actionRestaurar_BBDD.setText(_translate("MainWindow", "Restaurar BBDD"))
        self.actionbarSalir.setText(_translate("MainWindow", "barSalir"))
        self.actionbarSalir.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionbarAbrirCarpeta.setText(_translate("MainWindow", "barAbrirCarpeta"))
        self.actionbarAbrirCarpeta.setShortcut(_translate("MainWindow", "Alt+A"))
        self.actionbarCrearBackup.setText(_translate("MainWindow", "barCrearBackup"))
        self.actionbarRestaurarBackup.setText(_translate("MainWindow", "barRestaurarBackup"))
        self.actionbarImprimir.setText(_translate("MainWindow", "barImprimir"))
        self.actionImportar_Datos.setText(_translate("MainWindow", "Importar Datos"))
        self.actionExportar_Datos.setText(_translate("MainWindow", "Exportar Datos"))
