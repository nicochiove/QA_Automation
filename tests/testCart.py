from pages.cartPage import CartPage
from pages.products import ProductsPage

def test_redireccion_correcta_carrito(loginWithDriver):
    try:

        driver = loginWithDriver

        ProductsPage(driver).agregar_producto_al_carrito()
        ProductsPage(driver).navegar_a_carrito()
        
        assert '/cart.html' in driver.current_url, "La redirección al carrito no fue correcta"
    
    except Exception as e:
        print(f"Error en test_redireccion_correcta_carrito: {e}")
        raise
    finally:
        driver.quit()


def test_existe_al_menos_un_producto_en_carrito(loginWithDriver):
    try:
        driver = loginWithDriver

        ProductsPage(driver).agregar_producto_al_carrito()
        ProductsPage(driver).navegar_a_carrito()
        productoCarrito = CartPage(driver).buscar_producto_en_carrito()
        
        assert productoCarrito is not None, "Debería haber un al menos un Producto agregado al Carrito"

    except Exception as e:
        print(f"Error en test_existe_al_menos_un_producto_en_carrito: {e}")
        raise
    finally:
        driver.quit()

def test_producto_en_carrito_tiene_nombre_y_precio(loginWithDriver):
    try:
        driver = loginWithDriver

        nombreAgregado = ProductsPage(driver).agregar_producto_al_carrito_con_nombre()
        ProductsPage(driver).navegar_a_carrito()
        nombreCarrito = CartPage(driver).get_nombre_producto_en_carrito()
        precioProducto = CartPage(driver).get_precio_producto_en_carrito()
        
        assert nombreCarrito is not None, "El producto debería tener un nombre"
        assert nombreCarrito == nombreAgregado, "El producto en el carrito no es el mismo que se añadió"
        assert precioProducto is not None, "El producto debería tener un precio"

    except Exception as e:
        print(f"Error en test_producto_en_carrito_tiene_nombre_y_precio: {e}")
        raise
    finally:
        driver.quit()