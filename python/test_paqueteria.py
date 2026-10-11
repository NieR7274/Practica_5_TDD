import pytest

from python.paqueteria import Paqueteria

@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Paqueteria()

#Casos normales

@pytest.mark.parametrize("pesopquete", [1, 2, 3, 4, 5])
def test_Hasta_5kg_Estandar(pesopquete):

    resultado = sistema.Costo_Envio(pesopquete, "estandar")

    assert resultado == 50.00