import pytest
from SateliteNatural import SateliteNatural

class TestSateliteNatural:

    @pytest.fixture
    def setup_scenario1(self):
        """
        Construye un nuevo SateliteNatural vacío
        """
        return SateliteNatural("nombre", 0.1, 0.2)

    def test_editar(self, setup_scenario1):
        """
        Este método se encarga de verificar el método editar y la inicialización de los atributos en el método constructor.
        Objetivo: Probar la modificación de un satélite natural.
        Resultados esperados:
        1. Creación de un nuevo satélite natural con el nombre 'nombre' con excentricidad 0.1 e inclinación 0.2.
        2. Modificar los datos del satélite natural con el nombre 'nombre' con excentricidad 0.3 e inclinación 0.4.
        3. Verificar que los nuevos datos del satélite natural sean correctos.
        """
        satelite = setup_scenario1
        assert pytest.approx(satelite.dar_excentricidad(), 0.001) == 0.1, "La excentricidad es incorrecta"
        assert pytest.approx(satelite.dar_inclinacion(), 0.001) == 0.2, "La inclinación es incorrecta"
        satelite.cambiar_excentricidad(0.3)
        satelite.cambiar_inclinacion_orbital(0.4)
        assert pytest.approx(satelite.dar_excentricidad(), 0.001) == 0.3, "La excentricidad es incorrecta"
        assert pytest.approx(satelite.dar_inclinacion(), 0.001) == 0.4, "La inclinación es incorrecta"

    def test_obtener_excentricidad(self, setup_scenario1):
        """
        Este método se encarga de verificar el método obtenerExcentricidad.
        Objetivo: Probar que se creó correctamente el satélite natural.
        Resultados esperados:
        1. Obtener el valor correcto de la excentricidad.
        """
        satelite = setup_scenario1
        assert pytest.approx(satelite.dar_excentricidad(), 0.001) == 0.1, "La excentricidad es incorrecta"

    def test_obtener_inclinacion(self, setup_scenario1):
        """
        Este método se encarga de verificar el método obtenerInclinacion.
        Objetivo: Probar que se creó correctamente el satélite natural.
        Resultados esperados:
        1. Obtener el valor correcto de la inclinación.
        """
        satelite = setup_scenario1
        assert pytest.approx(satelite.dar_inclinacion(), 0.001) == 0.2, "La inclinación es incorrecta"

    def test_obtener_nombre(self, setup_scenario1):
        """
        Este método se encarga de verificar el método obtenerNombre.
        Objetivo: Probar que se creó correctamente el planeta.
        Resultados esperados:
        1. Obtener el valor correcto del nombre del planeta.
        """
        satelite = setup_scenario1
        assert satelite.dar_nombre() == "nombre", "El nombre es incorrecto"

if __name__ == '__main__':
    pytest.main()
