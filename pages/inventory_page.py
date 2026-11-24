
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos(self):
        logger.info("Obteniendo lista de productos del inventario")

        productos = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item"
        )

        logger.info(f"Productos encontrados: {len(productos)}")
        return productos

    def obtener_nombre_primer_producto(self):
        logger.info("Obteniendo nombre del primer producto")

        productos = self.obtener_productos()

        nombre = productos[0].find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        logger.info(f"Nombre del primer producto: {nombre}")
        return nombre

    def obtener_precio_primer_producto(self):
        logger.info("Obteniendo precio del primer producto")

        productos = self.obtener_productos()

        precio = productos[0].find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        logger.info(f"Precio del primer producto: {precio}")
        return precio

    def menu_visible(self):
        logger.info("Verificando visibilidad del menú")

        menu = self.driver.find_element(
            By.ID, "react-burger-menu-btn"
        )

        visible = menu.is_displayed()
        logger.info(f"Menú visible: {visible}")
        return visible

    def filtro_visible(self):
        logger.info("Verificando visibilidad del filtro")

    def agregar_producto(self, nombre):
        logger.info(f"Buscando producto para agregar: {nombre}")

        productos = self.obtener_productos()

        for producto in productos:
            nombre_producto = producto.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text

            if nombre_producto == nombre:
                producto.find_element(
                    By.TAG_NAME, "button"
                ).click()

                logger.info(f"Producto agregado al carrito: {nombre}")
                return

        logger.error(f"No se encontró el producto: {nombre}")
        raise AssertionError(f"No se encontró el producto: {nombre}")


    def obtener_contador_carrito(self):
        logger.info("Obteniendo contador del carrito")

        contador = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        logger.info(f"Cantidad de productos en el carrito: {contador.text}")
        return contador

    
    def ir_al_carrito(self):
        logger.info("Navegando hacia el carrito")

        self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        logger.info("Se ingresó al carrito correctamente")
