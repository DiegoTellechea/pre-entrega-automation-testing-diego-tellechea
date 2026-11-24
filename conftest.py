import pytest
from selenium import webdriver

import pytest_html
import pathlib
import base64


@pytest.fixture

def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
    

@pytest.fixture
def base_url():
    return "https://reqres.in/api" 

@pytest.fixture
def headers():
    return{
        "x-api-key": "pub_0ebf6955264676288e4f55f3237e138015c2a86c87e3032e9fffb026de6895f6"
        }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        # Solo generar captura si la prueba utiliza Selenium
        if driver is not None:

            carpeta = pathlib.Path("reports/screenshots")
            carpeta.mkdir(parents=True, exist_ok=True)

            archivo = carpeta / f"{item.name}.png"

            driver.save_screenshot(str(archivo))

            # Convertir imagen a Base64
            imagen = base64.b64encode(
                archivo.read_bytes()
            ).decode("utf-8")

            # Adjuntar captura al reporte HTML
            extras = getattr(report, "extras", [])
            extras.append(
                pytest_html.extras.png(
                    imagen,
                    name="Screenshot"
                )
            )

            report.extras = extras
