# Testing Automatizado de Swag Labs

## Propósito del Proyecto

Este proyecto tiene como objetivo evaluar de forma automatizada las funcionalidades principales del sitio web [Swag Labs](https://www.saucedemo.com/), incluyendo el flujo de autenticación (login), la visualización del inventario de productos y la gestión del carrito de compras. Las pruebas están diseñadas para validar la experiencia del usuario y el correcto funcionamiento de los componentes clave del sistema.

## Tecnologías

- **Python 3.11+**
- **Pytest** – Framework de testing
- **Selenium WebDriver** – Automatización de navegador
- **ChromeDriver** – Driver para Google Chrome
- **pytest-html** – Generación de reportes en formato HTML
- **VS Code** – Editor recomendado para desarrollo

## Setup del Proyecto

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repo.git
   cd nombre-del-repo
  
2. **Instalar Dependecias**
   ```bash
   pip install selenium pytest pytest-html
3. **Instalar ChromeDriver**
  Descargar version correspondiente desde https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419 y asegurarse que este en el PATH

## Ejecución de Pruebas

El proyecto se configuro para poder ejecutar todos los tests desarrollados de una vez, utilizando el archivo run_tests.py
  ```bash
  py run_tests.py
  ```
O podemos ejecutar los tests para cada uno de las páginas o modulos, ejecutando
  ```bash
  pytest tests/[ARCHIVO].py -v --html=reporte[MODULO].html
  ```
