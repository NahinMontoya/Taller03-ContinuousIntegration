from tallerEjecicio import calcular_descuentos, validar_cantidad_pedido


def test_calcular_descuentos_valido():
    pedido1 = {
        "Especiales Chef": (25, 5),
        "Comida Ecuatoriana": (7, 3)
    }
    assert calcular_descuentos(pedido1) == (106.4, 39.6)

def test_calcular_descuentos_fallido_calculo():
    pedido1 = {
        "Especiales Chef": (25, 5),
        "Comida Ecuatoriana": (7, 3)
    }
    assert calcular_descuentos(pedido1) != (121, 28)


def test_calcular_descuentos_fallido_SinDescuentoCantidad():
    pedido1 = {
        "Especiales Chef": (25, 2),
        "Comida Ecuatoriana": (7, 1)
    }
    assert calcular_descuentos(pedido1) == (47, 10)

def test_calcular_descuentos_fallido_SinDescuento():
    pedido1 = {
        "Especiales Chef": (12, 2),
        "Comida Ecuatoriana": (7, 1)
    }
    assert calcular_descuentos(pedido1) == (31, 0)

def test_validar_cantidad_pedido_valido():
    cantidad = "25"

    assert validar_cantidad_pedido(cantidad) == 25

def test_validar_cantidad_pedido_fallido_tipoSalida():
    cantidad = "25"

    assert validar_cantidad_pedido(cantidad) != "25"

def test_validar_cantidad_pedido_fallido_FueraDeRango():
    cantidad = "125"
    assert validar_cantidad_pedido(cantidad) == None

def test_validar_cantidad_pedido_fallido_DentroDeRango():
    cantidad = "99"
    assert validar_cantidad_pedido(cantidad) != None







