from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    URL = "https://www.saucedemo.com/cart.html"

    _CART_ITEM = (By.CLASS_NAME,"cart_item")
    # _INVENTORY_ITEM_NAME = (By.CLASS_NAME,"inventory_item_name ")
    # _INVENTORY_ITEM_PRICE = (By.CLASS_NAME,"inventory_item_price")
    # _ADD_TO_CART = (By.CSS_SELECTOR, ".pricebar > button")
    # _CANTIDAD_PRODS_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self,driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver,10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    