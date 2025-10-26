import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    service = Service() 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
