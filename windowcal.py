# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowcal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowcal(object):
    def setupUi(self, windowcal):
        windowcal.setObjectName("windowcal")
        windowcal.setWindowModality(QtCore.Qt.WindowModal)
        windowcal.resize(315, 188)
        windowcal.setModal(True)
        self.calendarWidget = QtWidgets.QCalendarWidget(windowcal)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 0, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(windowcal)
        QtCore.QMetaObject.connectSlotsByName(windowcal)

    def retranslateUi(self, windowcal):
        _translate = QtCore.QCoreApplication.translate
        windowcal.setWindowTitle(_translate("windowcal", "Calendario"))
