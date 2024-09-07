class MaquinaHelado:
    def __init__(self):
        self.estado = 'Apagada'
        self.tipo_producto = None
        self.sabor = None
        self.consistencia = None

    def iniciar_maquina(self):
        """Enciende la máquina"""
        self.estado = 'Encendida'

    def seleccionar_producto(self, tipo):
        """Selecciona el tipo de producto (Helado/Batido)"""
        if self.estado != 'Encendida':
            raise Exception("La máquina debe estar encendida para seleccionar un producto.")
        
        tipos_validos = ['Helado', 'Batido']
        tipo_formateado = tipo.title()
        if tipo_formateado not in tipos_validos:
            raise ValueError("Tipo de producto no válido.")
        
        self.tipo_producto = tipo_formateado
        self.consistencia = 'Media' if tipo_formateado == 'Helado' else 'Suave'
        self.estado = 'En Producción'

    def elegir_sabor(self, sabor):
        """Selecciona el sabor del producto"""
        sabores_validos = ['vainilla', 'dulce de leche', 'combinado']  # Todos en minúsculas
        sabor_formateado = sabor.lower()  # Convertir a minúsculas
        if sabor_formateado not in sabores_validos:
            raise ValueError("Sabor no válido.")
        self.sabor = sabor_formateado

    def servir_producto(self):
        """Sirve el producto si la máquina está encendida y en producción"""
        if self.consistencia == 'Cristalizado':
            self.estado = 'Apagada'
            raise ValueError("Consistencia 'Cristalizado' no permitida. La máquina se apaga.")
        if self.estado != 'En Producción':
            raise Exception("La máquina debe estar en producción para servir el producto.")
        
        print(f"Servido: {self.tipo_producto} con sabor {self.sabor} y consistencia {self.consistencia}.")
        self.estado = 'Apagada'