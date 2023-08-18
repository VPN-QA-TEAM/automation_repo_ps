import time

from selenium import webdriver
import pytest

@pytest.fixture()
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for chrome only
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")  # for chrome only
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    #driver.maximize_window()
    driver.get('https://portalmurid.com')
    request.cls.driver = driver
    yield
    driver.quit()


