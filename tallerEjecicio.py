def mostrar_programa_gastronomico():
    menu_principal = {
        "Comida Ecuatoriana": 7,
        "Comida Colombiana": 9,
        "Comida Peruana": 6,
        "Comida Venezolana": 3,
        "Comida China": 12,
        "Comida Italiana": 14,
        "Reposteria": 5,
        "Especiales Chef": 25,
    }
    print("                      **** Bienvenidos a nuestro Restaurant ****")
    print("**** Comidas de diferentes paises y especialidades disponibles en nuestro menu ****")
    print("Seleccione las comidas que necesita y disfrute de nuestra variedad de comidas")
    print("                           Estas son las opciones disponibles:")

    # Mostrar el menú y sus precios.
    for comida, precio in menu_principal.items():
        print(f"{comida}: ${precio}")

    return menu_principal



def calcular_descuentos(pedido):
    costo_total = 0
    cantidad_total=0
    for precio, cantidad in pedido.values():
        costo_total += precio * cantidad
        cantidad_total+=cantidad

    descuento = 0

    if cantidad_total > 20:
        descuento = costo_total * 0.2  # Descuento del 20% si hay más de 20 elementos en el pedido.
    elif cantidad_total > 5:
        descuento = costo_total * 0.1  # Descuento del 10% si hay más de 5 elementos en el pedido.

    if costo_total > 100:
        descuento += 25  # Descuento adicional de $25 si el costo total es mayor a $100.
    elif costo_total > 50:
        descuento += 10  # Descuento adicional de $10 si el costo total es mayor a $50.

    costo_total -= descuento

    #return round(costo_total,2), round(descuento,2)
    return costo_total, descuento


def validar_cantidad_pedido(cantidad):
    try:
        cantidad = int(cantidad)
        if cantidad > 0 and cantidad <= 100:
            return cantidad
    except ValueError:
        pass

    return None

def programa_gastronomico():
    menu = mostrar_programa_gastronomico()
    pedido = {}

    while True:
        comida = input("Ingrese el nombre de la comida : ").strip().title()

        if comida not in menu:
            print("¡Error! Comida no disponible en el menú.")
            continue

        cantidad_valida = False
        while not cantidad_valida:
            cantidad = input("Ingrese la cantidad de esta comida: ")
            cantidad_validada = validar_cantidad_pedido(cantidad)

            if cantidad_validada is None:
                print("¡Error! Cantidad no válida. Debe ser un número entero positivo menor o igual a 100.")
            else:
                cantidad_valida = True

        pedido[comida] = (menu[comida], cantidad_validada)  # Almacenar nombre de la comida y cantidad en una tupla.

        continuar_pedido = input("¿Desea continuar agregando más comidas al pedido? (Ingrese 'Sí' o 'No'): ").strip().lower()

        if continuar_pedido == 'no':
            break

    print("\nDetalles del pedido:")
    for comida, (precio, cantidad) in pedido.items():  # Desempaquetar el valor de la tupla.
        print(f"{comida}: {cantidad} x ${precio} = ${precio * cantidad}")  # Calcular el precio total por comida.
    costo_total, descuento = calcular_descuentos(pedido)
    print(f"\nCosto total: ${costo_total}")
    print(f"Descuento aplicado: ${descuento}")

    pedido_confirmacion = input("Su pedido se encuentra listo, ingrese OK para la confirmación: ").strip().lower()

    if pedido_confirmacion == "ok":
        print("Su pedido se realizó con éxito. ¡Gracias por preferirnos! Vuelva pronto.")
        return costo_total
    else:
        print("Su pedido ha sido cancelado.")
        return -1


#programa_gastronomico()
