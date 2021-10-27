import clients
import conexion
import var,events
from window import *
from PyQt5.QtWidgets import QMessageBox

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

    def cargaProv(self):
        try:
            var.ui.cmbProv.clear()
            prov=[" ","A Coruña","Lugo","Ourense","Pontevedra","Vigo"]
            for i in prov:
                var.ui.cmbProv.addItem(i)

        except Exception as error: print("Error en modulo cargaProv")

    def selProv(prov):
        try:
            Clientes.cargaMun(prov)
        except Exception as error: print("Error en modulo selProv")

    def cargaMun(prov):
        try:
            var.ui.cmbMun.clear()
            if prov == "Vigo":
                mun=[" ","Vigo","Redondela","Ponteareas","Cangas"]
            if prov == "A Coruña":
                mun=[" ","A Coruña","Ferrol","Betanzos","Santiago"]
            if prov == "Pontevedra":
                mun=[" ","Pontevedra","Moaña","Lalín","A Cañiza"]
            if prov == "Ourense":
                mun=[" ","Ourense","O Barco","Monforte","Verin"]
            if prov== "Lugo":
                mun=[" ","Lugo","Sarria","Villalba","Ribadeo"]
            for i in mun:
                var.ui.cmbMun.addItem(i)
        except Exception as error: print("Error en modulo cargaMun")

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
                cliente=[var.ui.txtDNI, var.ui.txtFecha, var.ui.txtNome, var.ui.txtApel,  var.ui.txtDir]
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
                row = 0
                column = 0
                var.ui.tabClientes.insertRow(row)
                for campo in tabCli:
                    cell = QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabClientes.setItem(row, column, cell)
                    column += 1
                print(newCli)
                conexion.Conexion.altaCli(newCli)
                Clientes.limpiaFormCli(self)
            except Exception as error:
                print('Error en guardar clientes')
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

    def cargaCLi(self):
        try:
            fila=var.ui.tabClientes.selectedItems()
            datos=[var.ui.txtDNI,var.ui.txtApel,var.ui.txtNome,var.ui.txtFecha]
            if fila:
                row=[dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])

            if 'Efctv' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Trfr' in row[4]:
                var.ui.chkTrans.setChecked(True)
            if 'Trjt' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if 'CrgCnt' in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)
        except Exception as error:
            print('Error al cargar datos de un cliente')