import mysql.connector

# Conexión a la base de datos
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  #usuario de Workbench
            password="7030",  #contraseña de Workbench
            database="maquina"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None

# Cerrar conexión
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

# Consultas de tipo SELECT

def obtener_estados(conexion):
    cursor = conexion.cursor()
    query = "SELECT * FROM Estado"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for estado in resultados:
        print(estado)
    cursor.close()

def obtener_tipos_producto(conexion):
    cursor = conexion.cursor()
    query = "SELECT * FROM TipoProducto"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for tipo in resultados:
        print(tipo)
    cursor.close()

def obtener_sabores(conexion):
    cursor = conexion.cursor()
    query = "SELECT * FROM Sabor"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for sabor in resultados:
        print(sabor)
    cursor.close()

def obtener_consistencias(conexion):
    cursor = conexion.cursor()
    query = "SELECT * FROM Consistencia"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for consistencia in resultados:
        print(consistencia)
    cursor.close()

def obtener_maquinas(conexion):
    cursor = conexion.cursor()
    query = """
        SELECT MaquinaHelado.id, Estado.nombre, TipoProducto.nombre, Sabor.nombre, Consistencia.nombre
        FROM MaquinaHelado
        JOIN Estado ON MaquinaHelado.id_estado = Estado.id
        JOIN TipoProducto ON MaquinaHelado.id_tipo = TipoProducto.id
        JOIN Sabor ON MaquinaHelado.id_sabor = Sabor.id
        JOIN Consistencia ON MaquinaHelado.id_consistencia = Consistencia.id
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    for maquina in resultados:
        print(maquina)
    cursor.close()