import pytest

from pages.userpage import UserPage
from faker import Faker

fake = Faker()

contact_number = '081111111111'
address = fake.address()

@pytest.mark.usefixtures("setup")
class TestUser:
    """-------------------------------------SCENARIO USER--------------------------------------------"""

    def test_add_new_user_teacher(self):
        user = UserPage(self.driver)
        user.goToAddUserPage("admin.uat", "password123*")
        user.clickTeacherAddUserRoleBtn()
        user.inputName("Depan", "Belakang", "depan.belakang")
        user.clickGenderDropdownField()
        user.clickGenderListOptionBtn("Male")  # input =  "Male" / "Female"
        user.clickReligionDropdownField()
        user.clickReligionListOptionBtn("Buddha")  # input =  Islam / Hindu / Katolik / Buddha / Protestan / Khonghucu
        user.inputContactNumber(contact_number)
        user.inputResidentialInfo(address, 'Jakarta', '939393')