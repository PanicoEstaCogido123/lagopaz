import var
from window import *
class Clientes():
    def validarDNI():
        try:
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
                        var.ui.lblValidoDNI.setText('Bien')
                    else:
                        var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                        var.ui.lblValidoDNI.setText('Mal')
                        var.ui.txtDNI.setStyleSheet("background-color:pink;")
            else:
                var.ui.lblValidoDNI.setStyleSheet('QLabel{color:red;}')
                var.ui.lblValidoDNI.setText('Mal')
                var.ui.txtDNI.setStyleSheet("background-color:pink;")
        except Exception as error:
            print('Error en validar DNI')
    def selSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print('Femenino')
            if var.ui.rbtMasc.isChecked():
                print('Masculino')
        except Exception as error:
            print('Error en el modulo SelSexo')

    def selPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print('Efectivo')
            if var.ui.chkTarjeta.isChecked():
                print('Tarjeta')
            if var.ui.chkCargoCuenta.isChecked():
                print('CargoCuenta')
            if var.ui.chkTrans.isChecked():
                print('Transferencia')
        except Exception as error:
            print('Error en el modulo selPago')

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
            print("Has seleccionado la provincia de "+prov)

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

    def selMun(mun):
        try:

            print("Has seleccionado el municipio de "+ mun)

        except Exception as error: print("Error en modulo selMun")

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