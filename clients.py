import conexion, var
from window import *
from PyQt5 import QtSql

class Clientes():
    def validarDNI():
        try:
            global resultado
            resultado=0
            dni=var.ui.txtDNI.text()
            tabla='TRWAGMYFPDXBNJZSQVHLCKE' #Letras DNI
            dig_ext='XYZ'                   #Letras NIE
            reemp_dig_ext={'X':'0','Y':'1','Z':'2'}
            numeros='1234567890'
            dni=dni.upper() #Convertir a mayusculas
            if len(dni)==9:
                    dig_control=dni[8]
                    dni=dni[:8]
                    if dni[0] in dig_ext:
                        dni=dni.replace(dni[0],reemp_dig_ext[dni[0]])
                    if len(dni)==len([n for n in dni if n in numeros])and tabla[int(dni)%23]==dig_control:
                        var.ui.lblValidoDNI.setStyleSheet('QLabel{color:green;}')
                        var.ui.lblValidoDNI.setText('V')
                        var.ui.txtDNI.setStyleSheet("background-color:white;")
                        resultado=1
                    else:
                        var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                        var.ui.lblValidoDNI.setText('X')
                        var.ui.txtDNI.setStyleSheet("background-color:pink;")
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                var.ui.lblValidoDNI.setText('X')
                var.ui.txtDNI.setStyleSheet("background-color:pink;")
        except Exception as error:
            print('Error en validar DNI')

    def cargaProv(prov):
        try:
            var.ui.cmbProv.clear()
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print("Error en modulo cargaProv")

    def cargaMun(mun):
        try:
            var.ui.cmbMun.clear()
            for i in mun:
                var.ui.cmbMun.addItem(i)
        except Exception as error:
            print("Error en modulo cargaMun")

    def cargarFecha(qDate):
        try:
            data=('{0}/{1}/{2}'.format(qDate.day(),qDate.month(),qDate.year()))
            var.ui.txtFecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error en modulo cargarFecha', error)

    def letraCapital():
        try:
            textoApel=var.ui.txtApel.text()
            textoNom = var.ui.txtNome.text()
            textoDir = var.ui.txtDir.text()
            var.ui.txtApel.setText(textoApel.title())
            var.ui.txtNome.setText(textoNom.title())
            var.ui.txtDir.setText(textoDir.title())
        except Exception as error:
            print('Error en validar DNI')

    def guardaCli(self):
        Clientes.validarDNI()
        if (resultado==1):
            try:
                #preparamos el registro
                newCli=[]#para la bbdd
                cliente=[var.ui.txtDNI, var.ui.txtFecha, var.ui.txtNome, var.ui.txtApel, var.ui.txtDir]
                tabCli=[]  # para la tablaWidget
                #recogemos datos
                client=[var.ui.txtDNI, var.ui.txtFecha, var.ui.txtNome, var.ui.txtApel]
                for i in cliente:
                    newCli.append(i.text())
                for i in client:
                    tabCli.append(i.text())
                newCli.append(var.ui.cmbProv.currentText())
                newCli.append(var.ui.cmbMun.currentText())
                if var.ui.rbtMasc.isChecked():
                    newCli.append('Hombre')
                else:
                    newCli.append('Mujer')
                pagos=[]
                if var.ui.chkEfectivo.isChecked():
                    pagos.append('Efctv ')
                if var.ui.chkTarjeta.isChecked():
                    pagos.append('Trjt ')
                if var.ui.chkCargoCuenta.isChecked():
                    pagos.append('CrgCnt')
                if var.ui.chkTrans.isChecked():
                    pagos.append('Trfr')
                tabCli.append('; '.join(pagos))
                newCli.append(';'.join(pagos))
                # Cargamos en la tabla
                conexion.Conexion.altaCli(newCli)
                conexion.Conexion.cargarTabCli()
                Clientes.limpiaFormCli(self)
            except Exception as error:
                print('Error en guardar clientes',error)
        else:
            popup = QtWidgets.QMessageBox()
            popup.setWindowTitle('Error')
            popup.setText('DNI invalido')
            popup.setIcon(QtWidgets.QMessageBox.Warning)
            popup.exec()

    def limpiaFormCli(self):
        try:
            registros=[var.ui.txtDNI, var.ui.txtNome, var.ui.txtApel, var.ui.txtFecha, var.ui.txtDir]
            for i in registros:
                i.setText('')
            var.ui.lblValidoDNI.setText('')
            var.ui.txtDNI.setStyleSheet("background-color:white;")
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtMasc.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.chkTrans.setChecked(False)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMun.setCurrentIndex(0)
        except Exception as error:
            print('Error en limpiar formulario')

    def cargaCli(self):
        try:
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.chkTrans.setChecked(False)
            fila = var.ui.tabClientes.selectedItems()
            if fila:
                row = [dato.text() for dato in fila]
                dni = row[0]
                query = QtSql.QSqlQuery()
                query.prepare(
                    'SELECT dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pagos FROM CLIENTES WHERE dni="' + dni + '"')
                if query.exec_():
                    while query.next():
                        dni = query.value(0)
                        alta = query.value(1)
                        apellidos = query.value(2)
                        nombre = query.value(3)
                        direccion = query.value(4)
                        provincia = query.value(5)
                        conexion.Conexion.CargaMun(provincia)
                        municipio = query.value(6)
                        sexo = query.value(7)
                        pago = query.value(8)
                var.ui.txtDNI.setText(dni)
                var.ui.txtApel.setText(apellidos)
                var.ui.txtNome.setText(nombre)
                var.ui.txtFecha.setText(alta)
                var.ui.txtDir.setText(direccion)
                var.ui.cmbProv.setCurrentText(provincia)
                var.ui.cmbMun.setCurrentText(municipio)
                if "Hombre" in sexo: var.ui.rbtMasc.setChecked(True)
                if "Mujer" in sexo: var.ui.rbtFem.setChecked(True)
                if "CrgCnt" in pago: var.ui.chkCargoCuenta.setChecked(True)
                if "Efctv" in pago: var.ui.chkEfectivo.setChecked(True)
                if "Trjt" in pago: var.ui.chkTarjeta.setChecked(True)
                if "Trfr" in pago: var.ui.chkTrans.setChecked(True)
        except Exception as error: print("Error en modulo CargaCli",error)

    def modifCli(self):
        try:
            modcliente = []
            cliente = [var.ui.txtDNI, var.ui.txtFecha,  var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            for i in cliente:
                modcliente.append(i.text())
            modcliente.append(var.ui.cmbProv.currentText())
            modcliente.append(var.ui.cmbMun.currentText())
            if var.ui.rbtMasc.isChecked():
                modcliente.append('Hombre')
            else:
                modcliente.append('Mujer')
            pagos = []
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efctv ')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Trjt ')
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('CrgCnt')
            if var.ui.chkTrans.isChecked():
                pagos.append('Trfr')
            modcliente.append(';'.join(pagos))
            conexion.Conexion.modifCli(modcliente)
            print(modcliente)
        except Exception as error:
            print('Error en modifCli', error)