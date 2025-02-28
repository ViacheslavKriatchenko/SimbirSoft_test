from selenium import webdriver
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
@allure.title("Подготовка к тесту, выбор браузера")
def driver():
    print('\nStart testing...')
    options = ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
    print('\nStop testing...')
