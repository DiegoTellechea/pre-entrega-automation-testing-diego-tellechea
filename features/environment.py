from selenium import webdriver


def before_scenario(context, scenario):
    print("Iniciando navegador...")
    context.driver = webdriver.Chrome()


def after_scenario(context, scenario):
    print("Cerrando navegador...")
    context.driver.quit()