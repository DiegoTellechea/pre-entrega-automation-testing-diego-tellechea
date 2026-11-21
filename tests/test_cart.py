from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_products_json


def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user","secret_sauce")

    # Leemos el primer producto del Json
    producto = read_products_json()[0]

    # Agregamos el producto del Json
    inventory_page.agregar_producto(producto["nombre"])

    assert inventory_page.obtener_contador_carrito().text == "1"

    # Ir al carrito

    inventory_page.ir_al_carrito()

    # Validar nombre contra el Json
    assert cart_page.get_product_name() == producto["nombre"]

    # Validar precio contra el Json
    assert cart_page.get_product_price() == producto["precio"]



