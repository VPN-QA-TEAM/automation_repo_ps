import time
import pytest
import modulefinder

from webdriver_manager.core import driver

from pages.subjectpage import SubjectPage
from pages.loginpage import LoginPage

NAMA_KELAS = 'Kelas 7'

@pytest.mark.usefixtures("setup")
class TestSubject:
    """-------------------------------------SCENARIO SUBJECT--------------------------------------------"""
    def test_create_new_kelas(self):
        login = LoginPage(self.driver)
        subject = SubjectPage(self.driver)
        login.userLogin("admin.uat", "password123*")
        subject.clickSkipEmailBtn()
        subject.clickSubjectSidebarsBtn()
        subject.verifySubjectPage()
        subject.clickCloseFloaterBtn()
        subject.clickTambahPembelajaranBtn()
        subject.verifyTambahPembelajaranModalTitle()
        subject.clickJenjangKelasField()
        subject.clickJenjangKelasListOption("7")
        subject.inputNamaPembelajaran("Test Automation")
        subject.clickDoneTambahPembelajaranBtn()



