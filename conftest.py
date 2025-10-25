import pytest
from selenium import webdriver
from pages.login import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def loginWithDriver(driver): 
    LoginPage(driver).abrir_pagina().login_completo("standard_user","secret_sauce")
    return driver