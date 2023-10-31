import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import LoginPage


class UserPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


########################################## LOCATORS ###########################################################################

    USER_SIDEBARS_BTN = '//li[@class="menu-item icon-user"]'  # by XPATH
    USER_SIDEBARS_ADDUSER_BTN = '//div[.="Tambah Pengguna Baru" or .="Add New User"]'  # by XPATH

    # LOCATORS - ADD USER

    STUDENT_TIPE_PENGGUNA_BTN = '//input[@id="student"]/parent::div[@class="d-flex mgt-custom-radio"]'  # by XPATH
    TEACHER_TIPE_PENGGUNA_BTN = '//input[@id="teacher"]/parent::div[@class="d-flex custom-control mgt-custom-radio"]'  # by XPATH
    ADMIN_TIPE_PENGGUNA_BTN = '//input[@id="admin"]/parent::div[@class="d-flex custom-control mgt-custom-radio"]'  # by XPATH
    FIRSTNAME_INPUT_FIELD = '//input[@name="firstName"]'  # by XPATH
    LASTNAME_INPUT_FIELD = '//input[@name="lastName"]'  # by XPATH
    USERNAME_INPUT_FIELD = '//input[@name="userName"]'  # by XPATH
    EMAIL_INPUT_FIELD = '//input[@name="email"]'  # by XPATH
    GENDER_DROPDOWN_FIELD = '//select[@id="gender-add-edit"]'  # by XPATH

    def genderOptionListBtn(self, gender):  # gender = "Male" or "Female"
        GENDER_DROPDOWN_LIST_BTN = '//option[@value="'+gender+'"]'  # by XPATH
        return GENDER_DROPDOWN_LIST_BTN

    RELIGION_DROPDOWN_FIELD = '//select[@id="religion-add-edit"]'  # by XPATH

    def religionOptionListBtn(self, religion):  # religion = Islam / Hindu / Katolik / Buddha / Protestan / Khonghucu
        RELIGION_DROPDOWN_LIST_BTN = '//option[@value="'+religion+'"]'  # by XPATH
        return RELIGION_DROPDOWN_LIST_BTN

    PHONE_NUMBER_INPUT_FIELD = '//input[@name="contactNumber"]'  # by XPATH
    PLACEOFBIRTH_INPUT_FIELD = '//input[@name="placeOfBirth"]'  # by XPATH
    DATEOFBIRTH_INPUT_FIELD = '//input[@name="dateOfBirth"]'  # by XPATH
    ADDRESS_INPUT_FIELD = '//textarea[@id="textarea-address"]'  # by XPATH
    CITY_INPUT_FIELD = '//input[@name="city"]'  # by XPATH
    POSTALCODE_INPUT_FIELD = '//input[@name="postcode"]'  # by XPATH
    TEACHERID_INPUT_FIELD = '//input[@name="teacherId"]'  # by XPATH (FOR TEACHER)
    NUPTK_INPUT_FIELD = '//input[@name="nuptk"]'  # by XPATH (FOR TEACHER)
    EMPLOYMENTSTATUS_DROPDOWN_FIELD = '//select[@id="employment-add-edit"]'  # by XPATH (FOR TEACHER)

    def employmentStatusOptionListBtn(self, status):  # status = pns / honorer / tetap (FOR TEACHER)
        EMPLOYMENTSTATUS_DROPDOWN_LIST_BTN = '//option[@value="'+status+'"]'  # by XPATH
        return EMPLOYMENTSTATUS_DROPDOWN_LIST_BTN

    NIP_INPUT_FIELD = '//input[@name="nip"]'  # by XPATH (FOR TEACHER)

    STUDENTID_INPUT_FIELD = '//input[@name="studentId"]'  # by XPATH (FOR STUDENT)
    NISN_INPUT_FIELD = '//input[@name="nisn"]'  # by XPATH (FOR STUDENT)
    NIS_INPUT_FIELD = '//input[@name="nis"]'  # by XPATH (FOR STUDENT)
    GRADE_DROPDOWN_INPUT_FIELD = '//select[@id="grade-add-edit"]'  # by XPATH (FOR STUDENT)

    def gradeOptionListBtn(self, course_name):  # course_name =  Course Name
        GRADE_DROPDOWN_LIST_BTN = '//option[.="'+course_name+'"]'  # by XPATH (FOR STUDENT)
        return GRADE_DROPDOWN_LIST_BTN

    CLASSSECTION_DROPDOWN_FIELD = '//select[@id="section-add-edit"]'  # by XPATH (FOR STUDENT)

    def classSectionOptionListBtn(self, class_section_name):  # class_section_name = Name of Class Section
        CLASSSECTION_DROPDOWN_LIST_BTN = '//option[.="'+class_section_name+'"]'  # by XPATH (FOR STUDENT)
        return CLASSSECTION_DROPDOWN_LIST_BTN

    JOINGRADE_INPUT_FIELD = '//input[@name="currentSchoolJoinGrade"]'  # by XPATH (FOR STUDENT)
    PREVIOUSSCHOOL_NAME_INPUT_FIELD = '//input[@name="previousSchoolName"]'  # by XPATH (FOR STUDENT)
    CURRENTSCHOOL_JOIN_DATE_FIELD = '//input[@name="currentSchoolJoinDate"]'  # by XPATH (FOR STUDENT)
    STATUSINFAMILY_INPUT_FIELD = '//input[@name="statusInFamily"]'  # by XPATH (FOR STUDENT)
    FATHERNAME_INPUT_FIELD = '//input[@name="fatherName"]'  # by XPATH (FOR STUDENT)
    FATHEROCCUPATION_INPUT_FIELD = '//input[@name="fatherOccupation"]'  # by XPATH (FOR STUDENT)
    PARENTSADDRESS_INPUT_FIELD = '//textarea[@name="parentAddress"]'  # by XPATH (FOR STUDENT)
    CHILDORDER_INFAMILY_INPUT_FIELD = '//input[@class="ae-updown"]'  # by XPATH (FOR STUDENT) NUMBER 1 - 99
    MOTHERNAME_INPUT_FIELD = '//input[@name="motherName"]'  # by XPATH (FOR STUDENT)
    MOTHEROCCUPATION_INPUT_FIELD = '//input[@name="motherOccupation"]'  # by XPATH (FOR STUDENT)