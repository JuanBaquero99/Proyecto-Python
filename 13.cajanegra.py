import unittest


def suma(num_1, num_2):
    return (num_1) + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self): #recibe de parametro el self que verifica la suma
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15) #Función para verificar que resultado si sea 15

    def test_suma_dos_negativos(self): #Recibe de parametro el self que verifica la suma
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17) #Función para verificar que el resultado si sea -15


if __name__ == '__main__':
    unittest.main()