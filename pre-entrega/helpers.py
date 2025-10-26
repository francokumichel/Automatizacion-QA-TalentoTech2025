from socket import timeout
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


def wait_for_element(driver, by, value, timeout=10):
    '''
    Espera hasta que un elemento esté presente en el DOM y sea visible.
    
    :param driver: Instancia del WebDriver.
    :param by: Estrategia para localizar el elemento (By.ID, By.XPATH, etc.).
    :param value: Valor utilizado con la estrategia de localización.
    :param timeout: Tiempo máximo de espera en segundos.
    :return: El elemento web si se encuentra, de lo contrario lanza una excepción TimeoutException.
    '''
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        return None
    
def wait_for_clickable(driver, by, value, timeout=10):
    '''
    Espera hasta que un elemento sea clickeable.
    
    :param driver: Instancia del WebDriver.
    :param by: Estrategia para localizar el elemento (By.ID, By.XPATH, etc.).
    :param value: Valor utilizado con la estrategia de localización.
    :param timeout: Tiempo máximo de espera en segundos.
    :return: El elemento web si se encuentra y es clickeable, de lo contrario lanza una excepción TimeoutException.
    '''
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        return element
    except TimeoutException:
        return None

def find_element(driver, by, value):
    '''
    Encuentra un elemento en la página.
    '''
    try:
        element = driver.find_element(by, value)
        return element
    except NoSuchElementException:
        return None

def find_elements(driver, by, value):
    '''
    Encuentra múltiples elementos en la página.
    '''
    try:
        elements = driver.find_elements(by, value)
        return elements
    except NoSuchElementException:
        return []
    
def login(driver, username, password):
    '''
    Realiza el login en la aplicación Saucedemo.
    
    :param driver: Instancia del WebDriver.
    :param username: Nombre de usuario para el login.
    :param password: Contraseña para el login.
    '''
    
    # Con esto navegamos a la página de login
    driver.get("https://www.saucedemo.com/")
    
    # Esperamos a que los campos de usuario y contraseña estén presentes, y los completamos
    user_input = wait_for_element(driver, By.ID, "user-name")
    user_input.send_keys(username)
    
    pass_input = wait_for_element(driver, By.ID, "password")
    pass_input.send_keys(password)
    
    login_button = wait_for_clickable(driver, By.ID, "login-button")
    login_button.click()

    print(f"{username} ha iniciado sesión!")

