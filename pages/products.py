from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:

    URL = "https://www.saucedemo.com/inventory.html"

    _INVENTORY_ITEM = (By.CLASS_NAME,"inventory_item")
    _INVENTORY_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name ")
    _INVENTORY_ITEM_PRICE = (By.CLASS_NAME,"inventory_item_price")
    _ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar > button")
    _CANTIDAD_PRODS_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def buscar_productos_existentes(self):
        product = self.wait.until(EC.visibility_of_element_located(self._INVENTORY_ITEM))
        return product
    
    def buscar_nombre_producto(self):
        nombreProducto = self.wait.until(EC.visibility_of_element_located(self._INVENTORY_ITEM_NAME))
        return nombreProducto

    def buscar_precio_producto(self):
        precioProducto = self.wait.until(EC.visibility_of_element_located(self._INVENTORY_ITEM_PRICE))
        return precioProducto
    
    def agregar_producto_al_carrito(self):
        addToCart = self.wait.until(EC.visibility_of_element_located(self._ADD_TO_CART))
        addToCart.click()
        return self
    
    def agregar_producto_al_carrito_con_nombre(self):
        addToCart = self.wait.until(EC.visibility_of_element_located(self._ADD_TO_CART))
        addToCart.click()
        
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self._INVENTORY_ITEM_NAME)).text

        return nombre_producto

    
    def buscar_cantidad_productos_en_carrito(self):
        cantidadProductos = self.wait.until(EC.visibility_of_element_located(self._CANTIDAD_PRODS_CARRITO)).text
        return int(cantidadProductos)
    
    def navegar_a_carrito(self):
        linkCarrito = self.wait.until(EC.visibility_of_element_located(self._CANTIDAD_PRODS_CARRITO))
        linkCarrito.click()
        return self