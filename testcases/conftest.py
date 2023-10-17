import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")  # for chrome only
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get('https://portalmurid.com')
    request.cls.driver = driver
    yield
    driver.quit()


