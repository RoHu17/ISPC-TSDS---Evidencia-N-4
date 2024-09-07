import database
from maquina import MaquinaHelado

def print_header(title):
    print("\n+" + "-"*58 + "+")
    print("|" + title.center(58) + "|")
    print("+" + "-"*58 + "+")

def mostrar_menu_principal(maquina):
    print_header("Menú Principal")
    print("| 1. Hacer helado o batido".ljust(60) + "|")
    print("| 2. Consultas sobre la máquina".ljust(60) + "|")
    print("| 3. Salir".ljust(60) + "|")
    print("+" + "-"*58 + "+")

def mostrar_menu_gestion(maquina):
    print_header("Gestión de la Máquina de Helados")
    if maquina.estado == 'Apagada':
        print("| 1. Encender la máquina y seleccionar producto".ljust(60) + "|")
    elif maquina.estado == 'Encendida' or maquina.estado == 'En Producción':
        print("| 1. Seleccionar producto (Helado/Batido)".ljust(60) + "|")
        print("| 2. Elegir sabor".ljust(60) + "|")
        print("| 3. Servir producto".ljust(60) + "|")
    print("| 4. Volver al menú principal".ljust(60) + "|")
    print("+" + "-"*58 + "+")

def mostrar_menu_consultas():
    print_header("Consultas a la Base de Datos")
    print("| 1. Ver tipos de productos".ljust(60) + "|")
    print("| 2. Ver sabores disponibles".ljust(60) + "|")
    print("| 3. Ver consistencias disponibles".ljust(60) + "|")
    print("| 4. Ver estados de las máquinas".ljust(60) + "|")
    print("| 5. Volver al menú principal".ljust(60) + "|")
    print("+" + "-"*58 + "+")

def gestionar_maquina(maquina):
    while True:
        mostrar_menu_gestion(maquina)
        opcion = input("Elija una opción: ").strip()
        
        if opcion == "1":
            if maquina.estado == 'Apagada':
                maquina.iniciar_maquina()  # Enciende la máquina
            tipo = input("Elija el producto ('Helado' o 'Batido'): ").strip().capitalize()
            try:
                maquina.seleccionar_producto(tipo)
                print(f"Producto seleccionado: {maquina.tipo_producto}")
            except Exception as e:
                print(e)
        elif opcion == "2":
            if maquina.estado == 'En Producción':
                sabor = input("Elija el sabor ('Vainilla', 'Dulce de Leche', 'Combinado'): ").strip()
                try:
                    maquina.elegir_sabor(sabor)
                    print(f"Sabor elegido: {maquina.sabor}")
                except Exception as e:
                    print(e)
            else:
                print("La máquina debe estar en producción para elegir el sabor.")
        elif opcion == "3":
            if maquina.estado == 'En Producción':
                try:
                    maquina.servir_producto()
                    print("Producto servido.")
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print(e)
            else:
                print("La máquina no está en producción. No se puede servir el producto.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida o no disponible en el estado actual de la máquina.")

def consultas_db():
    while True:
        mostrar_menu_consultas()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            productos = database.consultar_tipos_producto()
            print("Tipos de productos:", productos)
        elif opcion == "2":
            sabores = database.consultar_sabores()
            print("Sabores disponibles:", sabores)
        elif opcion == "3":
            consistencias = database.consultar_consistencias()
            print("Consistencias disponibles:", consistencias)
        elif opcion == "4":
            estados = database.consultar_estados()
            print("Estados de las máquinas:", estados)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")