from funciones_database import *  # Se importan todas la funciones del archivo 'funciones_database.py'
from funciones_validacion import *  # Se importan todas la funciones del archivo 'funciones_validacion.py'


# Declaro las funciones principales del menu
def menu_agregar_producto():
    while True:  # Empieza el ciclo y pido los datos al usuario
        print(
            "REGISTRO DE PRODUCTOS.\n" "Por favor complete con los datos del producto."
        )
        print(" ")
        nombre_producto = validar_nombre()
        descripcion = validar_descripcion()
        categoria = validar_categoria()
        cantidad = validar_cantidad()
        precio_unitario = validar_precio()
        # Diccionario donde se guardan los datos del producto
        producto = {
            "Nombre": nombre_producto,
            "Descripcion": descripcion,
            "Categoria": categoria,
            "Cantidad": cantidad,
            "Precio": precio_unitario,
        }
        # Llamo a la funcion 'db_agregar_producto()' y le paso como argumento el diccionario producto
        db_agregar_producto(producto)
        print(f"El producto se registró de manera exitosa {producto}")
        print()
        otro_producto = input("Desea agregar mas productos? (SI/NO): ").lower()
        if otro_producto != "si":
            break


def menu_buscar_producto():
    # Pide al usuario el Id de un producto y lo trae desde la base de datos
    while True:
        Id = input("Ingrese el Id del producto que quiere buscar: ")
        get_producto = db_buscar_producto(Id)
        if not get_producto:
            print(f"ERROR. No se encuentra ningun producto con ese Id")
        else:
            print(get_producto)
        print()
        continuar = input("Quiere buscar otro producto? (SI/NO): ").lower()
        if continuar != "si":
            break


def menu_mostrar_productos():
    while True:
        lista_productos = db_mostrar_productos()
        if lista_productos:
            for producto in lista_productos:
                print(producto)
        else:
            print("No hay productos para mostrar")
        print()
        volver_a_menu = input("Presione 'X' para cerrar y volver al menu: ").lower()
        if volver_a_menu == "x":
            break
        else:
            print()
            print("Opcion invalida. Presione 'X' para cerrar y volver al menu")
            print()


def menu_actualizar_producto():
    # Pide al usuario el Id de un producto y actualiza su cantidad
    while True:
        Id = input("Ingrese el Id del producto que quiere actualizar: ")
        get_producto = db_buscar_producto(Id)
        if not get_producto:
            print(f"ERROR. No se encuentra el producto con el Id {Id}")
        else:
            print(f"Producto encontrado: {get_producto[1]}")
            nueva_cantidad = int(
                input(f"Cantidad actual {get_producto[4]} - Nueva cantidad: ")
            )
            db_actualizar_producto_cantidad(Id, nueva_cantidad)
            print("Registro actualizado exitosamente!")
        continuar = input("Desea actualizar otro producto? (SI/NO): ").lower()
        if continuar != "si":
            break


def menu_eliminar_producto():
    while True:
        Id = input("Ingrese el Id del producto que quiere eliminar: ")
        get_producto = db_buscar_producto(Id)
        if not get_producto:
            print("ERROR. El producto no se encuentra")
        else:
            print(f"Se eliminara el siguiente producto: {get_producto}")
            confirmacion = input(
                "Desea eliminar de manera permanente el producto? (SI/NO): "
            ).lower()
            if confirmacion == "si":
                db_eliminar_producto(Id)
                print("Producto eliminado con éxito")
            else:
                print("Operación cancelada")
        continuar = input("Desea eliminar otro producto? (SI/NO): ").lower()
        if continuar != "si":
            break


def menu_reporte_stock():
    while True:
        minimo_stock = int(input("Ingrese el umbral de minimo stock: "))
        lista_productos = db_get_productos_by_condicion(minimo_stock)
        if not lista_productos:
            print(
                f"ERROR. No se han encontrado productos con stock menor a {minimo_stock}"
            )
        else:
            for producto in lista_productos:
                print(producto)
        volver_a_menu = input(
            "Desea realizar otra busqueda por stock? (SI/NO): "
        ).lower()
        if volver_a_menu != "si":
            break
