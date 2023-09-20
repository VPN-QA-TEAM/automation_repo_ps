import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class DashboardPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    SELAMAT_DATANG = '//div[@class="pageHeading"]/p/em'

    # TEST FUNCTION : OBJECT
    def getWelcomPage_on_Dashboard(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.SELAMAT_DATANG).text

    # TEST FUNCTION : ACTION/STEP


    # TEST FUNCTION : VERIFICATION/VALIDATION
    def verify_text_welcome_page(self, input_text_for_assert_in):
        text_dashboard = self.getWelcomPage_on_Dashboard()
        print(text_dashboard)
        assert input_text_for_assert_in in text_dashboard, "Not Same"