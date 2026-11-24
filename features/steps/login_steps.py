
from behave import given, when, then
from pages.login_page import LoginPage


@given("que el usuario este en la pagina del login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)
    context.driver.get("https://www.saucedemo.com/")


@when('ingresa en los campos "{usuario}" y "{contrasena}"')
def step_ingresar_credenciales(context, usuario, contrasena):
        
    if usuario == "VACIO":
        usuario = ""

    if contrasena == "VACIO":
        contrasena = ""
        
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_password(contrasena)


@when("hace click en el boton de login")
def step_click_login(context):
    context.login_page.hacer_click_login()


@then("deberia ingresar al inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url

@then('deberia mostrarse el mensaje de error "{mensaje}"')
def step_validar_mensaje_error(context,mensaje):
    error = context.login_page.get_error_message()
    assert mensaje in error, f"Se eperaba '{mensaje}', pero se obtuvo {error}"
