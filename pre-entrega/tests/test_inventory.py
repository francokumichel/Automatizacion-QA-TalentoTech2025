from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import wait_for_element, wait_for_clickable, is_element_displayed, login

def test_verify_catalog(driver):
    '''
    Test para verificar que el catálogo de productos se muestra correctamente después del login.
    
    :param driver: Instancia del WebDriver proporcionada por el fixture.
    '''
    login(driver, "standard_user", "secret_sauce")
    
    # Primer requerimiento: verificar que el título de la página de inventario sea correcto
    assert driver.title == "Swag Labs", f"El titulo de la página {driver.title} no es el esperado."

    print(f"El título de la página de inventario {driver.title} es correcto.")

    # Segundo requerimiento: comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert len(products) > 0, "No se encontraron productos visibles en la página."

    print(f"Se encontraron {len(products)} productos en la página de inventario.")
    print("Listado de productos:")
    for product in products:
        print("--------------------------------------------------------------------------------")
        print(f" - {product.text}")
        print("--------------------------------------------------------------------------------")

    # Tercer requerimiento: validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
    assert wait_for_element(driver, By.CLASS_NAME, "product_sort_container"), "El filtro de productos no está presente."
    assert wait_for_element(driver, By.ID, "react-burger-menu-btn"), "El menú lateral no está presente."
    assert wait_for_element(driver, By.CLASS_NAME, "shopping_cart_link"), "El ícono del carrito de compras no está presente."

    print("Elementos importantes de la interfaz están presentes en la página de inventario.")