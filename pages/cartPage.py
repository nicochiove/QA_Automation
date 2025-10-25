from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    _CART_ITEM = (By.CLASS_NAME,"cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name ")
    _CART_ITEM_PRICE = (By.CLASS_NAME,"inventory_item_price")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def buscar_producto_en_carrito(self):
        producto = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM))
        return producto
    
    def get_nombre_producto_en_carrito(self):
        nombreProd = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_NAME)).text
        return nombreProd
    
    def get_precio_producto_en_carrito(self):
        precio = self.wait.until(EC.visibility_of_element_located(self._CART_ITEM_PRICE)).text.replace("$",'')
        return float(precio)