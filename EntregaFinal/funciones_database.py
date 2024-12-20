import sqlite3

# Creo una variable global que indica cual sera la ruta
ruta_db = r"C:\Users\micae\Desktop\T.T CURSO PYTHON\TPfinal\EntregaFinal\Inventario.db"

"""
db_crear_tabla_productos() sera la funcion que crea/conecta con la base de datos para crear la tabla de Productos usando sqlite3

"""


def db_crear_tabla_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute(
        """
CREATE TABLE IF NOT EXISTS Productos(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Nombre TEXT NOT NULL,
Descripcion TEXT,
Categoria TEXT NOT NULL,
Cantidad INTEGER NOT NULL,
Precio REAL NOT NULL)
"""
    )
    conexion.commit()
    conexion.close()


"""
db_agregar_producto() sera la funcion encargada de registrar los productos en la DB
"""


def db_agregar_producto(producto):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "INSERT INTO Productos(Nombre, Descripcion, Categoria, Cantidad, Precio) VALUES (?, ?, ?, ?, ?)"
    placeholder = (
        producto["Nombre"],
        producto["Descripcion"],
        producto["Categoria"],
        producto["Cantidad"],
        producto["Precio"],
    )
    cursor.execute(query, placeholder)
    conexion.commit()
    conexion.close()


"""
db_buscar_producto() sera la funcion encargada de realizar las busquedas
"""


def db_buscar_producto(Id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM Productos WHERE Id = ?"
    placeholder = (Id,)
    cursor.execute(query, placeholder)
    # Obtengo los resultados de busqueda
    resultados_de_busqueda = cursor.fetchone()
    conexion.close()
    return resultados_de_busqueda


"""
db_listar_productos() sera la funcion que muestre todos los productos
"""


def db_mostrar_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM Productos"
    cursor.execute(query)
    # Obtengo los resultados de busqueda
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos


"""
db_actualizar_producto_cantidad() funcion para actualizar la cantidad de un producto segun el Id
"""


def db_actualizar_producto_cantidad(Id, nueva_cantidad):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "UPDATE Productos SET Cantidad = ? WHERE Id = ?"
    placeholder = (nueva_cantidad, Id)
    cursor.execute(query, placeholder)
    conexion.commit()
    conexion.close()


"""
db_eliminar_producto() elimina un producto especifico segun el Id
"""


def db_eliminar_producto(Id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "DELETE FROM Productos WHERE Id = ?"
    placeholder = (Id,)
    cursor.execute(query, placeholder)
    conexion.commit()
    conexion.close()


def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM Productos WHERE Cantidad < ?"
    placeholder = (minimo_stock,)
    cursor.execute(query, placeholder)
    lista_productos = cursor.fetchall()
    conexion.close()
    return lista_productos
