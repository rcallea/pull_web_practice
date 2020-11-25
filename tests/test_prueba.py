import sys
sys.path.append('src/cc')
from logica.prueba import Prueba
#from src.cc.logica.prueba import Prueba
import unittest

class test_devcuentasclaras(unittest.TestCase):
  
  def test_paraAsegurarnosQueFunciona(self):
    self.assertEqual(1,1)


  def test_nombrePrueba(self):
  	pr = Prueba()
  	self.assertNotEqual(pr.darNombre(),'Hola')
