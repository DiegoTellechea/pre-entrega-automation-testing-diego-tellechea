from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_products_json
from utils.logger import logger


def test_cart(driver):
    try:
        logger.info("Iniciando prueba del carrito")

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina de SauceDemo abierta correctamente")

        login_page.login("standard_user", "secret_sauce")
        logger.info("Login realizado correctamente")

        # Leemos el primer producto del JSON
        producto = read_products_json()[0]
        logger.info(f"Producto seleccionado del JSON: {producto['nombre']}")

        # Agregamos el producto del JSON
        inventory_page.agregar_producto(producto["nombre"])
        logger.info("Producto agregado al carrito")

        assert inventory_page.obtener_contador_carrito().text == "1"
        logger.info("Contador del carrito validado correctamente")

        # Ir al carrito
        inventory_page.ir_al_carrito()
        logger.info("Navegacion al carrito realizada correctamente")

        # Validar nombre contra el JSON
        assert cart_page.get_product_name() == producto["nombre"]
        logger.info("Nombre del producto validado correctamente")

        # Validar precio contra el JSON
        assert cart_page.get_product_price() == producto["precio"]
        logger.info("Precio del producto validado correctamente")

        logger.info("Prueba del carrito finalizada correctamente")

    except Exception:
        logger.exception("Error durante la prueba del carrito")
        raise




