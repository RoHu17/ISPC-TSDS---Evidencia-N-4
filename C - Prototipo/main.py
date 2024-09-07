from menu import mostrar_menu_principal, gestionar_maquina, consultas_db
from maquina import MaquinaHelado

def main():
    # Instancia la máquina de helado con parámetros predeterminados
    maquina = MaquinaHelado()  
    
    while True:
        # Muestra el menú principal y pasa la máquina como argumento
        mostrar_menu_principal(maquina)  
        opcion = input("Elija una opción: ")

        if opcion == "1":
            gestionar_maquina(maquina)
        elif opcion == "2":
            consultas_db()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()