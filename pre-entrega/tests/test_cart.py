from selenium.webdriver.common.by import By
from helpers import find_elements, login, wait_for_clickable, wait_for_element

def test_cart_funcionality(driver):
    '''
    Test para verificar la funcionalidad del carrito de compras.
    
    :param driver: Instancia del WebDriver proporcionada por el fixture.
    '''
    login(driver, "standard_user", "secret_sauce")

    # Primero verificamos que el carrito esté vacío inicialmente
    assert not wait_for_element(driver, By.CLASS_NAME, "shopping_cart_badge", 5), "El carrito debería estar vacío al iniciar sesión."

    # Buscamos el primer producto y verificamos su presencia
    products = find_elements(driver, By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No se encontraron productos para agregar al carrito."

    # Agregamos el primer producto al carrito
    first_product = products[0]
    first_product_name = first_product.text.splitlines()[0]
    add_to_cart_button = first_product.find_element(By.TAG_NAME, "button")
    add_to_cart_button.click()
    print(f"Producto agregado al carrito: {first_product_name}")

    # Verificamos que el ícono del carrito muestre 1 artículo
    cart_badge = wait_for_element(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", f"El carrito debería mostrar 1 artículo, pero muestra {cart_badge.text}"
    
    # Navegamos al carrito de compras
    cart_icon = wait_for_clickable(driver, By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    # Comprobamos que el producto agregado esté en el carrito
    cart_items = find_elements(driver, By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, f"El carrito debería tener 1 artículo, pero tiene {len(cart_items)}"

    cart_item_name = find_elements(driver, By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    assert cart_item_name[0].text == first_product_name, "El producto en el carrito no coincide con el producto agregado."
    print("Funcionalidad del carrito de compras verificada con éxito.")