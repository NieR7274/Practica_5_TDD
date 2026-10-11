import pytest

from python.paqueteria import Paqueteria

@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Paqueteria()


@pytest.mark.parametrize("pesoPaquete", [1, 2, 3, 4, 5])
def test_Costo_Paquete_Pequeno_Estandar(sistema,pesoPaquete):

    resultado = sistema.Costo_Envio(pesoPaquete, "estandar")

    assert resultado == 50.00

@pytest.mark.parametrize("pesoPaquete, precioEsperado", [
    (6, 60.00),
    (10, 100.00),
    (20, 200.00),
    (50, 500.00),
    (100, 1000.00)
])
def test_Costo_Paquete_Pesado_Estandar(sistema,pesoPaquete, precioEsperado):

    resultado = sistema.Costo_Envio(pesoPaquete, "estandar")

    assert resultado == precioEsperado

def test_Costo_Paquete_Pequeno_Expres(sistema):

    resultado = sistema.Costo_Envio(1, "expres")
    assert resultado == 100.00

@pytest.mark.parametrize("pesoPaquete, precioEsperado", [
    (6, 120.00),
    (10, 200.00),
    (20, 400.00),
    (50, 1000.00),
    (100, 2000.00)
])
def test_Costo_Paquete_Pesado_Expres(sistema,pesoPaquete, precioEsperado):

    resultado = sistema.Costo_Envio(pesoPaquete, "expres")

    assert resultado == precioEsperado

def test_Peso_Negativo(sistema):

    with pytest.raises(ValueError):
        sistema.Costo_Envio(-1, "estandar")

def test_Peso_Cero(sistema):

    with pytest.raises(ValueError):
        sistema.Costo_Envio(0, "expres")

def test_Tipo_Envio_Invalido(sistema):

    with pytest.raises(ValueError):
        sistema.Costo_Envio(5, "urgente")