import time
import pytest
import modulefinder

from pages.subjectpage import SubjectPage
from pages.dashboard import DashboardPage
from pages.loginpage import LoginPage
from testcases import test_login


@pytest.mark.usefixtures("setup")
class TestSubject:
    """-------------------------------------SCENARIO SUBJECT--------------------------------------------"""
    def testCobaLogin(self):
        login = LoginPage(self.driver)
        subject = SubjectPage(self.driver)
        login.userLogin("admin.uat", "password123*")
        subject.clickSkipEmailBtn()
        subject.clickSubjectSidebarsBtn()
        subject.verifySubjectPage()
