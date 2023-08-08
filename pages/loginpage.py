import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    USERID_FIELD = 'login'      # by id
    PASSWD_FIELD = 'password'   # by id
    LOGIN_BUTTON = '//button[@type="submit" and text()="Masuk"]'    # By.XPATH
    TOAST_LOGIN = '//div[@class="errorMsgBox show"]'    # By.XPATH

    '''CREATE FUNCTION to RETURN OBJECT'''
    def getUserIdField(self):
        return self.wait15sec_until_element_is_presence(By.ID, self.USERID_FIELD)
        # atau bisa jika dirasa tdk perlu wait : return self.driver.find_element(By.ID, self.USERID_FIELD)

    def getPasswordField(self):
        return self.wait15sec_until_element_is_presence(By.ID, self.PASSWD_FIELD)

    def getLoginButton(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.LOGIN_BUTTON)

    def getToastLogin(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.TOAST_LOGIN)


    '''CREATE ACTION METHOD '''
    def inputUserId(self, input_userid):
        self.getUserIdField().send_keys(input_userid)
        time.sleep(0.8)

    def inputPassword(self, input_passwd):
        self.getPasswordField().send_keys(input_passwd)
        time.sleep(0.8)

    def clickLoginButton(self):
        self.getLoginButton().click()
        time.sleep(0.5)

    def verify_toast_failed_login(self, input_validation_message):
        validation_msg = self.getToastLogin().text
        assert validation_msg == input_validation_message


