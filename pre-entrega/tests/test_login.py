import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import login

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce") 
])
def test_login_successful(driver, username, password):
    '''
    Caso de prueba: Login exitoso para diferentes usuarios.
    :param driver: Instancia del WebDriver proporcionada por el fixture.
    :param username: Nombre de usuario.
    :param password: Contraseña.
    '''
    driver.get("https://www.saucedemo.com/")
    login(driver, username, password)

    # Validamos login exitoso verificando que se haya redirigido a la página de inventario
    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
    
    assert "inventory.html" in driver.current_url, "No se redirigió a la página de inventario"

    print(f"Prueba de login exitoso para {username}")

@pytest.mark.exception
def test_login_locked_out_user(driver):
    """
    Test etiquetado como 'exception' que verifica el mensaje de error
    al intentar iniciar sesión con un usuario bloqueado.
    """
    driver.get("https://www.saucedemo.com/")
    login(driver, "locked_out_user", "secret_sauce")

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text

    assert "sorry, this user has been locked out" in error_message.lower(), (
        f"Mensaje de error incorrecto o no mostrado. Se obtuvo: '{error_message}'"
    )

    print("Prueba de usuario bloqueado completada con éxito.")
