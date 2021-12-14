import os

from reportlab.pdfgen import canvas

import informes


class Informes():

    def listadoClientes(self):
        cv = canvas.Canvas("informes/listadoClientes.pdf")
        cv.setFont("Courier-Oblique", 10)
        #Cabecera
        xMargenIzquierdo=25
        xMargenDerecho=575
        i = 0
        cv.line(xMargenIzquierdo,800,xMargenDerecho,800)
        textos=["Linea uno","Linea dos","Linea tres","Linea 4","Linea 5"]
        finTextos=textos.__len__()
        print(finTextos)
        while i!=finTextos:
            texto=textos[i]
            cv.drawString(25, 780-(i*10), texto)
            i+=1
        yLineaFinCabecera=780-finTextos*10
        cv.line(xMargenIzquierdo, yLineaFinCabecera, xMargenDerecho, yLineaFinCabecera)
        cv.save()

        rootPath = ".\\informes"
        cont = 0
        for file in os.listdir(rootPath):
            if file.endswith(".pdf"):
                os.startfile("%s/%s" % (rootPath, file))
                cont += 1
        '''
        try:
            cv = canvas.Canvas("informes/listadoClientes.pdf")
            self.cabecera(self)
            cv.drawString(100,750,"Listado Clientes")
            i=0

            while(i!=3000):
                i+=5
                x=i*2
                cv.line(30, 0, 400-x, 300+i)
                cv.circle(100-i*2,750-i*2,80-i/0.5,stroke=1,fill=0)

            text="Esto es un parrafo de prueba"
            cv.setFont("Courier-Oblique",10)
            cv.drawCentredString(150,650,text)
            cv.save()
            rootPath = ".\\informes"
            cont=0
            for file in os.listdir(rootPath):
                if file.endswith(".pdf"):
                    os.startfile("%s/%s"%(rootPath,file))
                    cont+=1
        except Exception as error:
            print("Error al generar el informe listadoClientes"+error)
    '''
    def cabecera(self):
        try:
            cv = canvas.Canvas("informes/listadoClientes.pdf")
            cv.line(40,800,500,800)
            cv.setFont("Helvetica-Oblique", 14)
            cv.drawString(50,585,"Import-ExportVigo")
            cv.setFont("Helvetica-Oblique", 10)
            cv.drawString(50, 770, "CIF: A00000000H")
            cv.line(40, 700, 500, 700)
        except Exception as error:
            print("Error al generar cabecera de listadoClientes"+error)