import unittest
from PyQt5 import QtSql

import clients
import conexion
import img.var


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_conexion(self):
        value = conexion.Conexion.db_connect(img.var.filedb)
        msg = 'Proba Errónea'
        self.assertTrue(value, msg)

    def test_dni(self):
        subfac = 0.00
        dni = '35580909R'
        value = clients.Clientes.validarDNI(str(dni))
        msg = 'Proba Errónea'
        self.assertTrue(value, msg)

    def test_fact(self):
        valor = 40.03
        codfac = 91
        try:
            msg = 'Calculos incorrectos'

        except Exception as error:
            print('Error listado de la tabla de vantas', error)
        self.assertEqual(round(float(valor), 2), round(float))

if __name__ == '__main__':
    unittest.main()
