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
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(460, 210, 111, 20))
        self.lblClientes.setObjectName("lblClientes")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(330, 340, 31, 16))
        self.lblDNI.setObjectName("lblDNI")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 340, 113, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 340, 47, 13))
        self.label.setObjectName("label")
        self.txtDatos = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDatos.setGeometry(QtCore.QRect(325, 241, 133, 20))
        self.txtDatos.setObjectName("txtDatos")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(325, 267, 75, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(325, 296, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuAbrir = QtWidgets.QMenu(self.menuArchivo)
        self.menuAbrir.setObjectName("menuAbrir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGuadar = QtWidgets.QAction(MainWindow)
        self.actionGuadar.setObjectName("actionGuadar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionFichero = QtWidgets.QAction(MainWindow)
        self.actionFichero.setObjectName("actionFichero")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuAbrir.addAction(self.actionFichero)
        self.menuArchivo.addAction(self.menuAbrir.menuAction())
        self.menuArchivo.addAction(self.actionGuadar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblClientes.setText(_translate("MainWindow", "XESTION CLIENTES"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAbrir.setTitle(_translate("MainWindow", "Abrir"))
        self.actionGuadar.setText(_translate("MainWindow", "Guadar"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como"))
        self.actionFichero.setText(_translate("MainWindow", "Fichero"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
