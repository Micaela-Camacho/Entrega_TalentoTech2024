def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("ERROR. No se admite dato nulo. Por favor ingrese un nombre")
        else:
            return nombre


def validar_descripcion():
    while True:
        descripcion = input("Ingrese una breve descripcion del producto: ").strip()
        return descripcion


def validar_categoria():
    while True:
        categoria = input("Ingrese la categoria del producto: ").strip()
        if not categoria:
            print(
                "ERROR. No se admite dato nulo. Por favor ingrese la categoria del producto"
            )
        else:
            return categoria


def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de producto: ").strip())
            if not cantidad:
                print("No se admite dato nulo. Ingrese la cantidad: ")
            else:
                return cantidad
        except ValueError:
            print("Tipo de dato no valido. Por favor ingrese la cantidad de producto")


def validar_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: ").strip())
            if not precio:
                print("No se admite dato nulo. Ingrese el precio del producto")
            else:
                return precio
        except ValueError:
            print("Tipo de dato invalido. Por favor ingrese el precio del producto")
