import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/testLogin.py",
    "tests/testInventory.py",
    "tests/testCart.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=reportes/reporteGeneral.html","--self-contained-html","-v"]

pytest.main(pytest_args)