from funciones_menu import *  # importar todas las funciones del archivo funciones_menu.py
from funciones_database import (
    db_crear_tabla_productos,
)  # importar la funcion db_crear_tabla_productos del archivo funciones_database.py


# Definir la funcion principal main
def main():
    # Iniciar la base de datos para que se conecte o cree la tabla segun sea el caso
    db_crear_tabla_productos()
    # Desarrollar la funcion main
    while True:
        print("-" * 20)
        print("BIENVENIDO..")
        print("-" * 20)
        print("MENU PRINCIPAL")
        print(
            "1.Registrar producto\n"
            "2.Consultar producto\n"
            "3.Mostrar listado de productos\n"
            "4.Actualizar producto\n"
            "5.Eliminar producto\n"
            "6.Resporte de stock\n"
            "7. Salir"
        )
        print(" ")
        opcion_elegida = input(
            "Que operación desea realizar? Ingrese la opcion correspondiente: "
        )
        print(" ")
        if opcion_elegida == "1":
            menu_agregar_producto()

        elif opcion_elegida == "2":
            menu_buscar_producto()

        elif opcion_elegida == "3":
            menu_mostrar_productos()

        elif opcion_elegida == "4":
            menu_actualizar_producto()

        elif opcion_elegida == "5":
            menu_eliminar_producto()

        elif opcion_elegida == "6":
            menu_reporte_stock()

        elif opcion_elegida == "7":
            break
        else:
            print("Opcion invalida")


main()
