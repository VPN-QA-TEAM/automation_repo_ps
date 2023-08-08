import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    # Sync issues
    def wait15sec_until_element_is_clickable(self, locator_type_by, web_element):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((locator_type_by, web_element)))
        return element

    def wait15sec_until_element_is_presence(self, locator_types, web_elementt):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.presence_of_element_located((locator_types, web_elementt)))
        return element

    def wait_for_presence_of_all_elementSS(self, locator_type_by, web_element):
        wait = WebDriverWait(self.driver, 20)
        list_elementS = wait.until(EC.presence_of_all_elements_located((locator_type_by, web_element)))
        return list_elementS

    # screenshot handling

    # others