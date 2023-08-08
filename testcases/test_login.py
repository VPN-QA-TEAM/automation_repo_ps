import time
import pytest
from pages.loginpage import LoginPage
from pages.dashboard import DashboardPage

valid_userid_Admin = "Admin00"
invalid_userid = "xasa111"
valid_passwd_Admin = "portal327"
invalid_passwd = "xccxfef111"
blank_field = ""


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_input_invalid_Password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(valid_userid_Admin)
        tl.inputPassword(invalid_passwd)
        tl.clickLoginButton()
        tl.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_input_invalid_UserID(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(invalid_userid)
        tl.inputPassword(valid_passwd_Admin)
        tl.clickLoginButton()
        tl.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_input_invalid_UserID_and_Password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(invalid_userid)
        tl.inputPassword(invalid_passwd)
        tl.clickLoginButton()
        tl.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_input_blank_UserID(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(blank_field)
        tl.inputPassword(valid_passwd_Admin)
        tl.clickLoginButton()
        tl.verify_toast_failed_login('Nama Pengguna kosong')

    def test_input_blank_Password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(valid_userid_Admin)
        tl.inputPassword(blank_field)
        tl.clickLoginButton()
        tl.verify_toast_failed_login('Kata Sandi kosong')


    def test_input_blankUserID_and_BlankPassword(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(blank_field)
        tl.inputPassword(blank_field)
        tl.clickLoginButton()
        tl.verify_toast_failed_login('Nama Pengguna & Kata Sandi kosong')

    def test_input_valid_userid_Admin_and_valid_password(self):
        tl = LoginPage(self.driver)
        tl.inputUserId(valid_userid_Admin)
        tl.inputPassword(valid_passwd_Admin)
        tl.clickLoginButton()
        dp = DashboardPage(self.driver)
        dp.verify_text_welcome_page('Selamat datang')



