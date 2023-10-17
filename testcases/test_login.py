import time
import pytest
from pages.loginpage import LoginPage
from pages.dashboard import DashboardPage

USERID_ADMIN_VALID = "admin.uat"
VALID_PASSWORD_ADMIN = "password123*"
USERID_GURU_MATPELK13_VALID = "teacher.k13"
VALID_PASSWORD_GURU_MATPELK13 = "password123*"
USERID_GURU_WALIK13_VALID = "teacher.km"
VALID_PASSWORD_GURU_WALIK13 = "password123*"

USERID_GURU_MATPELKM_VALID = "sub_teacher_k13"
VALID_PASSWORD_GURU_MATPELKM = "password123*"
USERID_GURU_WALIKM_VALID = "sub_teacher_km"
VALID_PASSWORD_GURU_WALIKM = "password123*"

USERID_STUDENT_K13_VALID = "student.01"
VALID_PASSWORD_STUDENT_K13 = "password123*"
USERID_STUDENT_KM_VALID = "student.11"
VALID_PASSWORD_STUDENT_KM = "password123*"

USERID_INVALID = "USERID_INVALID@*#"
INVALID_PASSWORD = "INVALID_PASS123*#"
BLANK_INPUT = ""

@pytest.mark.usefixtures("setup")
class TestLogin:
    """-------------------------------------SCENARIO LOGIN BY ADMIN--------------------------------------------"""
    def test_admin_login_valid_userid_and_valid_password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_ADMIN_VALID)
        admin.inputPassword(VALID_PASSWORD_ADMIN)
        admin.clickLoginButton()
        dashboard = DashboardPage(self.driver)
        dashboard.verify_text_welcome_page('Selamat datang')
        
    
    def test_admin_login_invalid_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_ADMIN_VALID)
        admin.inputPassword(INVALID_PASSWORD)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_admin_login_invalid_UserID(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_INVALID)
        admin.inputPassword(VALID_PASSWORD_ADMIN)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_admin_login_invalid_UserID_and_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_INVALID)
        admin.inputPassword(INVALID_PASSWORD)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_admin_login_blank_UserID(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(BLANK_INPUT)
        admin.inputPassword(VALID_PASSWORD_ADMIN)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Nama Pengguna kosong')

    def test_admin_login_blank_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_ADMIN_VALID)
        admin.inputPassword(BLANK_INPUT)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Kata Sandi kosong')

    def test_admin_login_blankUserID_and_blankPassword(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(BLANK_INPUT)
        admin.inputPassword(BLANK_INPUT)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Nama Pengguna & Kata Sandi kosong')

    """-------------------------------------SCENARIO LOGIN BY SUBJECT TEACHER K13-----------------------------------"""
    def test_teacher_MPk13_login_invalid_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_GURU_MATPELK13_VALID)
        admin.inputPassword(INVALID_PASSWORD)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_teacher_MPk13_login_invalid_UserID(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_INVALID)
        admin.inputPassword(VALID_PASSWORD_GURU_MATPELK13)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_teacher_MPk13_login_invalid_UserID_and_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_INVALID)
        admin.inputPassword(INVALID_PASSWORD)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_teacher_MPk13_login_blank_UserID(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(BLANK_INPUT)
        admin.inputPassword(VALID_PASSWORD_GURU_MATPELK13)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Nama Pengguna kosong')

    def test_teacher_MPk13_login_blank_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_GURU_MATPELK13_VALID)
        admin.inputPassword(BLANK_INPUT)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Kata Sandi kosong')

    def test_teacher_MPk13_login_blankUserID_and_blankPassword(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(BLANK_INPUT)
        admin.inputPassword(BLANK_INPUT)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Nama Pengguna & Kata Sandi kosong')

    def test_teacher_MPk13_login_valid_userid_and_valid_password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_GURU_MATPELK13_VALID)
        admin.inputPassword(VALID_PASSWORD_GURU_MATPELK13)
        admin.clickLoginButton()
        dashboard = DashboardPage(self.driver)
        dashboard.verify_text_welcome_page('Selamat datang')


    """-------------------------------------SCENARIO LOGIN BY STUDENT K13-------------------------------------------"""
    def test_student_k13_login_invalid_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_STUDENT_K13_VALID)
        admin.inputPassword(INVALID_PASSWORD)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_student_k13_login_invalid_UserID(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_INVALID)
        admin.inputPassword(VALID_PASSWORD_STUDENT_K13)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_student_k13_login_invalid_UserID_and_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_INVALID)
        admin.inputPassword(INVALID_PASSWORD)
        admin.clickLoginButton()
        admin.verify_toast_failed_login("Nama Pengguna atau Kata Sandi Salah")

    def test_student_k13_login_blank_UserID(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(BLANK_INPUT)
        admin.inputPassword(VALID_PASSWORD_STUDENT_K13)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Nama Pengguna kosong')

    def test_student_k13_login_blank_Password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_STUDENT_K13_VALID)
        admin.inputPassword(BLANK_INPUT)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Kata Sandi kosong')

    def test_student_k13_login_blankUserID_and_blankPassword(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(BLANK_INPUT)
        admin.inputPassword(BLANK_INPUT)
        admin.clickLoginButton()
        admin.verify_toast_failed_login('Nama Pengguna & Kata Sandi kosong')

    def test_student_k13_login_valid_userid_and_valid_password(self):
        admin = LoginPage(self.driver)
        admin.inputUserId(USERID_STUDENT_K13_VALID)
        admin.inputPassword(VALID_PASSWORD_STUDENT_K13)
        admin.clickLoginButton()
        dashboard = DashboardPage(self.driver)
        dashboard.verify_text_welcome_page('Selamat datang')