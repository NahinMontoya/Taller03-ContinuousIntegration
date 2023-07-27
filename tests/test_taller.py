from unittest.mock import patch

from tallerEjecicio import *

def test_mostrar_programa_gastronomico():
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
    assert mostrar_programa_gastronomico()== menu_principal
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

def test_calcular_descuentos_fallido_SinDescuentoMas20():
    pedido1 = {
        "Especiales Chef": (10, 20),
        "Comida Ecuatoriana": (7, 1)
    }
    assert calcular_descuentos(pedido1) == (140.6, 66.4)

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

def test_validar_cantidad_pedido_ValuueError():
    assert validar_cantidad_pedido('a') == None


def test_programa_gastronomico_Valido():
    inputs = [
        'Comida Colombiana',  # Comida
        '2',  # Cantidad válida
        'Si',  # Continuar agregando más comidas
        'Comida Ecuatoriana',  # Comida
        '4',  # Cantidad válida
        'No',  # Finalizar pedido
        'OK',  # Confirmación del pedido
    ]

    def mocked_input(prompt):
        return inputs.pop(0)

    @patch('builtins.input', side_effect=mocked_input)
    def test_programa_gastronomico(mock_input):
        result = programa_gastronomico()
        assert result == 41.4

    test_programa_gastronomico()

def test_programa_gastronomico_Fallido_ComidaNoMenu():
    inputs = [
        'Comida Chilena',  # Comida
        '2',  # Cantidad válida
        'Si',  # Continuar agregando más comidas
        'Comida Ecuatoriana',  # Comida
        '4',  # Cantidad válida
        'No',  # Finalizar pedido
        'OK',  # Confirmación del pedido
    ]

    def mocked_input(prompt):
        return inputs.pop(0)

    @patch('builtins.input', side_effect=mocked_input)
    def test_programa_gastronomico(mock_input):
        result = programa_gastronomico()
        assert result == -1

    test_programa_gastronomico()

def test_programa_gastronomico_Fallido_ComidaFueraRango():
    inputs = [
        'Comida Colombiana',  # Comida
        '200',  # Cantidad válida
        'Si',  # Continuar agregando más comidas
        'Comida Ecuatoriana',  # Comida
        '100',  # Cantidad válida
        'No',  # Finalizar pedido
        'OK',  # Confirmación del pedido
    ]

    def mocked_input(prompt):
        return inputs.pop(0)

    @patch('builtins.input', side_effect=mocked_input)
    def test_programa_gastronomico(mock_input):
        result = programa_gastronomico()
        assert result == -1

    test_programa_gastronomico()