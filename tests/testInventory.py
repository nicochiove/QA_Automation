from pages.products import ProductsPage

def test_title_correcto(loginWithDriver):
    try:
        driver = loginWithDriver

        assert driver.title == 'Swag Labs'
    
    except Exception as e:
        print(f"Error en test_title_correcto: {e}")
        raise
    finally:
        driver.quit()

def test_existe_al_menos_un_producto(loginWithDriver):
    try:
        driver = loginWithDriver

        producto = ProductsPage(driver).buscar_productos_existentes()
        nombre = ProductsPage(driver).buscar_nombre_producto()
        precio = ProductsPage(driver).buscar_precio_producto()

        assert producto is not None, "Debería existir al menos un Producto en el inventario"
        assert nombre is not None, "Debería existir un Producto con su respectivo Nombre"
        assert precio is not None, "Debería existir un Producto con su respectivo Precio"

    except Exception as e:
        print(f"Error en test_existe_al_menos_un_producto: {e}")
        raise
    finally:
        driver.quit()

def test_agregar_producto_al_carrito(loginWithDriver):
    try:

        driver = loginWithDriver

        ProductsPage(driver).agregar_producto_al_carrito()
        cantProductos = ProductsPage(driver).buscar_cantidad_productos_en_carrito()

        assert cantProductos == 1, "Debería haber un producto añadido al carrito"
    
    except Exception as e:
        print(f"Error en test_agregar_producto_al_carrito: {e}")
        raise
    finally:
        driver.quit()
