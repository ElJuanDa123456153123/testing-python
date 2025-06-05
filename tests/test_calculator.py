import unittest

from src.calculator import suma, resta, multiplicacion

class CalculatorTest(unittest.TestCase):
    
    #prueba unitaria para la funcion suma
    def test_suma(self):
        self.assertEqual(suma(4, 3), 7)
        
    def test_resta(self):
        self.assertEqual(resta(4, 3), 1)
        
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)
        
