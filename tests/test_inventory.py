from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory(driver):
    try:
        logger.info("Iniciando prueba de inventario")

        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Pagina de SauceDemo abierta correctamente")

        login_page.login("standard_user", "secret_sauce")
        logger.info("Login realizado correctamente")

        productos = inventory_page.obtener_productos()
        logger.info(f"Productos encontrados: {len(productos)}")

        assert len(productos) > 0
        logger.info("Validacion de cantidad de productos correcta")

        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        logger.info("Nombre del primer producto validado")

        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Precio del primer producto validado")

        assert inventory_page.menu_visible
        logger.info("Menu visible correctamente")

        assert inventory_page.filtro_visible
        logger.info("Filtro visible correctamente")

        logger.info("Prueba de inventario finalizada correctamente")

    except Exception:
        logger.exception("Error durante la prueba de inventario")
        raise
    