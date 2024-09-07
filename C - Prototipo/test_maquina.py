import unittest
from maquina import MaquinaHelado

class TestMaquinaHelado(unittest.TestCase):

    def setUp(self):
        """Inicializa una máquina de helado para las pruebas"""
        self.maquina = MaquinaHelado()
        self.maquina.iniciar_maquina()
        self.maquina.seleccionar_producto('helado')

    def test_iniciar_maquina(self):
        """Prueba que la máquina se inicie correctamente"""
        self.maquina.iniciar_maquina()
        self.assertEqual(self.maquina.estado, 'Encendida')

    def test_seleccionar_producto(self):
        """Prueba la selección de producto"""
        self.maquina.iniciar_maquina()
        self.maquina.seleccionar_producto('helado')
        self.assertEqual(self.maquina.tipo_producto, 'Helado')
        self.assertEqual(self.maquina.consistencia, 'Media')

    def test_elegir_sabor(self):
        """Prueba la elección de sabor"""
        self.maquina.iniciar_maquina()
        self.maquina.seleccionar_producto('batido')
        self.maquina.elegir_sabor('Vainilla')
        self.assertEqual(self.maquina.sabor, 'vainilla')

    def test_servir_producto(self):
        self.maquina.iniciar_maquina()
        self.maquina.seleccionar_producto('Helado')
        self.maquina.elegir_sabor('dulce de leche')  
        self.maquina.servir_producto()


    def test_consistencia_erronea(self):
        """Prueba el manejo de consistencia cristalizada"""
        self.maquina.iniciar_maquina()
        self.maquina.seleccionar_producto('batido')
        self.maquina.elegir_sabor('combinado')
        self.maquina.consistencia = 'Cristalizado'
        with self.assertRaises(ValueError) as context:
            self.maquina.servir_producto()
        self.assertEqual(str(context.exception), "Consistencia 'Cristalizado' no permitida. La máquina se apaga.")
        self.assertEqual(self.maquina.estado, 'Apagada')

if __name__ == '__main__':
    unittest.main()
