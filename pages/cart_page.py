
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_name(self):
        logger.info("Obteniendo nombre del producto en el carrito")

        nombre = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        ).text

        logger.info(f"Nombre del producto obtenido: {nombre}")
        return nombre

    def get_product_price(self):
        logger.info("Obteniendo precio del producto en el carrito")

        precio = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_price")
            )
        ).text

        precio_float = float(precio.replace("$", ""))

        logger.info(f"Precio del producto obtenido: {precio_float}")
        return precio_float

