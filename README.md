# Entrega_TalentoTech2024

## Inventario de Productos

### Descripción
Este proyecto Python es una aplicación de línea de comandos que permite gestionar un inventario de productos. Usa SQLite como base de datos para almacenar la información de los productos y ofrece distintas funcionalidades como:

* **Registro de productos:** Permite agregar nuevos productos al inventario.
* **Consulta de productos:** Permite buscar productos por su ID.
* **Listado de productos:** Muestra todos los productos registrados.
* **Actualización de productos:** Permite modificar la cantidad de un producto.
* **Eliminación de productos:** Permite eliminar un producto del inventario.
* **Reporte de stock:** Genera un reporte de los productos con un stock inferior a un umbral determinado.

### Instalación
1. **Clona el repositorio:**
   ```
   ```
### Uso
1. **Ejecuta el programa:**
   ```
    python main.py
   ```
2. **Sigue las instrucciones en pantalla:** El programa te presentará un menú con las diferentes opciones disponibles.

### Estructura del proyecto
* **main.py:** Contiene el punto de entrada del programa y la lógica principal de la aplicación.
* **funciones_menu.py:** Define las funciones que interactúan con el usuario a través del menú.
* **funciones_database.py:** Contiene las funciones que interactúan con la base de datos SQLite.
* **funciones_validacion.py:** Define las funciones para validar los datos ingresados por el usuario.
* **Inventario.db:** La base de datos SQLite donde se almacenan los datos de los productos.

