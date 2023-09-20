import time
import pytest
from pages.loginpage import LoginPage
from pages.dashboard import DashboardPage

USERID_ADMIN_VALID = "admin_uat"
USERID_ADMIN_INVALID = "ADMIN_UAAAATTTXXX"
VALID_PASSWORD_ADMIN = "password123*"
INVALID_PASSWORD_ADMIN = "xccxfef111"
BLANK_INPUT = ""


@pytest.mark.usefixtures("setup")
class TestLogin:

    """-------------------------------------SCENARIO LOGIN BY ADMIN--------------------------------------------"""
    def test_input_invalid_Password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(USERID_ADMIN_VALID)
        tl.inputPassword(INVALID_PASSWORD_ADMIN)
        tl.clickLoginButton()
        tl.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_input_invalid_UserID(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(USERID_ADMIN_INVALID)
        tl.inputPassword(VALID_PASSWORD_ADMIN)
        tl.clickLoginButton()
        tl.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_input_invalid_UserID_and_Password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(USERID_ADMIN_INVALID)
        tl.inputPassword(INVALID_PASSWORD_ADMIN)
        tl.clickLoginButton()
        tl.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_input_blank_UserID(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(BLANK_INPUT)
        tl.inputPassword(VALID_PASSWORD_ADMIN)
        tl.clickLoginButton()
        tl.verify_toast_failed_login('Nama Pengguna kosong')

    def test_input_blank_Password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(USERID_ADMIN_VALID)
        tl.inputPassword(BLANK_INPUT)
        tl.clickLoginButton()
        tl.verify_toast_failed_login('Kata Sandi kosong')


    def test_input_blankUserID_and_BlankPassword(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(BLANK_INPUT)
        tl.inputPassword(BLANK_INPUT)
        tl.clickLoginButton()
        tl.verify_toast_failed_login('Nama Pengguna & Kata Sandi kosong')

    def test_input_valid_userid_Admin_and_valid_password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(USERID_ADMIN_VALID)
        tl.inputPassword(VALID_PASSWORD_ADMIN)
        tl.clickLoginButton()
        dp = DashboardPage(self.driver)
        dp.verify_text_welcome_page('Selamat datang')
        # ---

    """-------------------------------------SCENARIO LOGIN BY TEACHER--------------------------------------------"""


