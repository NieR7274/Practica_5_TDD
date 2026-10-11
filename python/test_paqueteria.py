import pytest

from python.paqueteria import Paqueteria

@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Paqueteria()

#Casos normales

@pytest.mark.parametrize("pesoPaquete", [1, 2, 3, 4, 5])
def test_Hasta_5kg_Estandar(sistema,pesoPaquete):

    resultado = sistema.Costo_Envio(pesoPaquete, "estandar")

    assert resultado == 50.00

@pytest.mark.parametrize("pesoPaquete, precioEsperado", [
    (6, 60.00),
    (10, 100.00),
    (20, 200.00),
    (50, 500.00),
    (100, 1000.00)
])
def test_Mas_5kg_Estandar(sistema,pesoPaquete, precioEsperado):

    resultado = sistema.Costo_Envio(pesoPaquete, "estandar")

    assert resultado == precioEsperado