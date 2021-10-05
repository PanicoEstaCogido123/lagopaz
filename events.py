'''

Fichero de eventos generales

'''
import sys,var

class Eventos():
    def Salir(selfself):
        try:
            sys.exit()
        except Exception as error:
            print('Error en módulo salir ',error)