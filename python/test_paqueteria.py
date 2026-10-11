import pytest

from python.paqueteria import Paqueteria

@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Paqueteria()