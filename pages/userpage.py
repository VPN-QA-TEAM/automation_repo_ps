import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import LoginPage
from pages.subjectpage import SubjectPage


class UserPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


########################################## LOCATORS ###########################################################################

    USER_SIDEBARS_BTN = '//li[@class="menu-item icon-user"]'  # by XPATH
    USER_SIDEBARS_ADDUSER_BTN = '//div[.="Tambah Pengguna Baru" or .="Add New User"]'  # by XPATH
    USER_SIDEBARS_USERPAGE_BTN = '//span[.="Pengguna" or .="Users"]/parent::div[@class="profile-left"]'  # by XPATH

    # LOCATORS - ADD USER

    STUDENT_ROLE_BTN = '//label[@class="cursorPointer custom-control-label" and @for="student"]'  # by XPATH
    TEACHER_ROLE_BTN = '//label[@class="cursorPointer custom-control-label" and @for="teacher"]'  # by XPATH
    ADMIN_ROLE_BTN = '//label[@class="cursorPointer custom-control-label" and @for="admin"]'  # by XPATH
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
    RESIDENTIALINFO_ACCORDION_MENU = '//p[.="Informasi Tempat Tinggal" or .="Residential Information"]/ancestor::div[@class="pc-header cursorPointer accordion-addEditUser"]'  # by XPATH
    ADDRESS_INPUT_FIELD = '//textarea[@id="textarea-address"]'  # by XPATH
    CITY_INPUT_FIELD = '//input[@name="city"]'  # by XPATH
    POSTALCODE_INPUT_FIELD = '//input[@name="postcode"]'  # by XPATH
    CANCEL_BTN = '//div[@class="btn ae-button-cancel "]'  # by XPATH
    CREATE_BTN = '//button[@class="btn btn-primary ae-button-create "]'  # by XPATH

    # LOCATORS - ADD USER (TEACHER & ADMIN)

    TEACHERID_INPUT_FIELD = '//input[@name="teacherId"]'  # by XPATH (FOR TEACHER)
    NUPTK_INPUT_FIELD = '//input[@name="nuptk"]'  # by XPATH (FOR TEACHER)
    EMPLOYMENTSTATUS_DROPDOWN_FIELD = '//select[@id="employment-add-edit"]'  # by XPATH (FOR TEACHER)

    def employmentStatusOptionListBtn(self, status):  # status = pns / honorer / tetap (FOR TEACHER)
        EMPLOYMENTSTATUS_DROPDOWN_LIST_BTN = '//option[@value="'+status+'"]'  # by XPATH
        return EMPLOYMENTSTATUS_DROPDOWN_LIST_BTN

    NIP_INPUT_FIELD = '//input[@name="nip"]'  # by XPATH (FOR TEACHER)

    # LOCATORS - ADD USER (STUDENT)

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
    PARENTSMOBILEPHONE_INPUT_FIELD = '//input[@name="parentMobile"]'  # by XPATH (FOR STUDENT)
    GUARDIANNAME_INPUT_FIELD = '//input[@name="guardianName"]'  # by XPATH (FOR STUDENT)
    GUARDIANADDRESS_INPUT_FIELD = '//textarea[@name="guardianAddress"]'  # by XPATH (FOR STUDENT)
    GUARDIANOCCUPATION_INPUT_FIELD = '//input[@name="guardianOccupation"]'  # by XPATH (FOR STUDENT)
    GUARDIANMOBILEPHONE_INPUT_FIELD = '//input[@name="guardianMobile"]'  # by XPATH (FOR STUDENT)

    # LOCATORS - USERS MANAGEMENT PAGE

    STUDENT_CATEGORY_NAVBAR = '//a[.="Peserta Didik" or .="Student"]/ancestor::div[@class="nav-item"]'  # by XPATH
    TEACHER_CATEGORY_NAVBAR = '//a[.="Guru" or .="Teacher"]/ancestor::div[@class="nav-item"]'  # by XPATH
    ADMIN_CATEGORY_NAVBAR = '//a[.="Admin" or .="Administrator"]/ancestor::div[@class="nav-item"]'  # by XPATH
    PARENT_CATEGORY_NAVBAR = '//a[.="Orang Tua/Wali" or .="Parent"]/ancestor::div[@class="nav-item"]'  # by XPATH
    SEARCH_INPUT_FIELD = '//input[@name="searchTemp"]'  # by XPATH
    CREATENEWUSER_BTN = '//button[@class="btn btn-primary font-weight-medium py-3 mx-2 d-flex align-items-center"]'  # by XPATH
    CHECKALL_CHECKBOX = '//input[@type="checkbox"]/ancestor::th[1]'  # by XPATH
    YES_DELETE_CONFIRMATION_BTN = '//button[@class="btn yesDeleteMeeting  "]'  # by XPATH
    CANCEL_DELETE_CONFIRMATION_BTN = '//button[@class=" btn noDeleteMeeting  "]'  # by XPATH

    def userCheckbox(self, user_full_name):
        USER_CHECKBOX = '//span[.="' + user_full_name + '"]/ancestor::td/parent::tr//input[@type="checkbox"]'  # by XPATH
        return USER_CHECKBOX

    def userEditBtn(self, user_full_name):
        USER_EDIT_BTN = '//span[.="'+user_full_name+'"]/ancestor::td/parent::tr//button[.="Ubah" or .="Edit"]'  # by XPATH
        return USER_EDIT_BTN

    def userThreeDotsBtn(self, user_full_name):
        USER_THREEDOTS_BTN = '//span[.="'+user_full_name+'"]/ancestor::td/parent::tr//div[@id="dropdownAction"]'  # by XPATH
        return USER_THREEDOTS_BTN

    SELECTCOURSEFILTER_DROPDOWN_FIELD = '//option[.="Select Course" or .="Pilih Pembelajaran"]/parent::select[@class="select-filter form-control"]'  # by XPATH (FOR STUDENT & TEACHER)

    def courseOptionListBtn(self, course_name):
        COURSE_DROPDOWN_LIST_BTN = '//option[.="' + course_name + '"]'  # by XPATH (FOR STUDENT & TEACHER)
        return COURSE_DROPDOWN_LIST_BTN

    COURSESECTIONFILTER_DROPDOWN_FIELD = '//option[.="Select Section" or .="Pilih Kelas"]/parent::select[@class="select-filter form-control"]'  # by XPATH (FOR STUDENT & TEACHER)

    def sectionClassOptionListBtn(self, class_section):
        SECTIONCLASS_DROPDOWN_LIST_BTN = '//option[.="' + class_section + '"]'  # by XPATH (FOR STUDENT & TEACHER)
        return SECTIONCLASS_DROPDOWN_LIST_BTN

    # LOCATORS - USERS MANAGEMENT PAGE (STUDENT)

    def studentNis(self, student_name):
        STUDENT_NIS = '//span[.="'+student_name+'"]/ancestor::td/parent::tr//td[2]'  # by XPATH (FOR STUDENT)
        return STUDENT_NIS

    # LOCATORS - USERS MANAGEMENT PAGE (TEACHER)

    SUBJECTFILTER_DROPDOWN_FIELD = '//option[.="Select Subject" or .="Pilih Mata Pelajaran"]/parent::select[@class="select-filter form-control"]'  # by XPATH (FOR TEACHER)

    def subjectOptionListBtn(self, subject_name):
        SUBJECT_DROPDOWN_LIST_BTN = '//option[.="' + subject_name + '"]'  # by XPATH (FOR TEACHER)
        return SUBJECT_DROPDOWN_LIST_BTN

    def teacherNip(self, teacher_name):
        TEACHER_NIP = '//span[.="'+teacher_name+'"]/ancestor::td/parent::tr//td[2]'  # by XPATH (FOR TEACHER)
        return TEACHER_NIP

    # LOCATORS - USERS MANAGEMENT PAGE (PARENT)

    GENERATE_PARENT_ACCOUNT_BTN = '//button[.="Generate Parent Accounts" or .="Buat Akun Orang Tua"]'  # by XPATH (FOR PARENT)
    FAMILY_GROUP_BTN = '//button[.="Grup Keluarga" or .="Family Group"]'  # by XPATH (FOR PARENT)

    def generateParentAccontBtn(self, student_name):
        GENERATE_PARENT_ACCOUNT_BTN = '//div[.="'+student_name+'"]/ancestor::tr//button[.="Buat Akun" or .="Generate"]'  # by XPATH (FOR PARENT)
        return GENERATE_PARENT_ACCOUNT_BTN

    def parentThreeDotsActionBtn(self, student_name):
        THREEDOTS_ACTION_BTN = '//div[.="'+student_name+'"]/ancestor::tr//div[@id="dropdownAction"]'  # by XPATH (FOR PARENT)
        return THREEDOTS_ACTION_BTN

    def blockParentAccountBtn(self, student_name):
        BLOCKPARENTACCOUNT_BTN = '//div[.="'+student_name+'"]/ancestor::tr//span[@class="dropdown-item cursorPointer"][1]'  # by XPATH (FOR PARENT)
        return BLOCKPARENTACCOUNT_BTN

    def resetPasswordParentAccountBtn(self, student_name):
        RESETPASSWORD_PARENTACCOUNT_BTN = '//div[.="'+student_name+'"]/ancestor::tr//span[@class="dropdown-item cursorPointer"][2]'  # by XPATH (FOR PARENT)
        return RESETPASSWORD_PARENTACCOUNT_BTN

    def deleteParentAccountBtn(self, student_name):
        DELETE_PARENTACCOUNT_BTN = '//div[.="'+student_name+'"]/ancestor::tr//div[@class="actionIcon" and @title="Remove Parent Accounts"]'  # by XPATH (FOR PARENT)
        return DELETE_PARENTACCOUNT_BTN

###############################################################################################################################

    def getUserSidebarBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.USER_SIDEBARS_BTN)

    def getAddUserOptionBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.USER_SIDEBARS_ADDUSER_BTN)

    def getTeacherAddUserRoleBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.TEACHER_ROLE_BTN)

    def getFirstNameField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.FIRSTNAME_INPUT_FIELD)

    def getLastNameField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.LASTNAME_INPUT_FIELD)

    def getUserNameField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.USERNAME_INPUT_FIELD)

    def getGenderDropdownField(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.GENDER_DROPDOWN_FIELD)

    def getGenderListOptionBtn(self, gender):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.genderOptionListBtn(gender))

    def getReligionDropdownField(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.RELIGION_DROPDOWN_FIELD)

    def getReligionListOptionBtn(self, religion):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.religionOptionListBtn(religion))

    def getContactNumberField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.PHONE_NUMBER_INPUT_FIELD)

    def getResidentialAccordionMenu(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.RESIDENTIALINFO_ACCORDION_MENU)

    def getAddressInputField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.ADDRESS_INPUT_FIELD)

    def getCityInputField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.CITY_INPUT_FIELD)

    def getPostalCodeInputField(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.POSTALCODE_INPUT_FIELD)

###############################################################################################################################

    def clickUserSidebarBtn(self):
        self.getUserSidebarBtn().click()

    def clickAddUserOptionBtn(self):
        self.getAddUserOptionBtn().click()

    def clickTeacherAddUserRoleBtn(self):
        self.getTeacherAddUserRoleBtn().click()

    def inputFirstName(self, first_name):
        self.getFirstNameField().send_keys(first_name)

    def inputLastName(self, last_name):
        self.getLastNameField().send_keys(last_name)

    def inputUserName(self, userName):
        self.getUserNameField().send_keys(userName)

    def clickGenderDropdownField(self):
        self.getGenderDropdownField().click()
        time.sleep(0.2)

    def clickGenderListOptionBtn(self, gender):
        self.getGenderListOptionBtn(gender).click()

    def clickReligionDropdownField(self):
        self.getReligionDropdownField().click()
        time.sleep(0.2)

    def clickReligionListOptionBtn(self, religion):
        self.getReligionListOptionBtn(religion).click()

    def inputContactNumber(self, phone_number):
        self.getContactNumberField().send_keys(phone_number)

    def clickResidentialAccordionMenu(self):
        self.getResidentialAccordionMenu().click()
        time.sleep(0.3)

    def inputAddress(self, address):
        self.getAddressInputField().send_keys(address)

    def inputCity(self, city):
        self.getCityInputField().send_keys(city)

    def inputPostalCode(self, postal_code):
        self.getPostalCodeInputField().send_keys(postal_code)

###############################################################################################################################

    def goToAddUserPage(self, username, password):
        login = LoginPage(self.driver)
        subject = SubjectPage(self.driver)
        login.userLogin(username, password)
        time.sleep(0.5)
        subject.clickSkipEmailBtn()
        time.sleep(0.2)
        self.clickUserSidebarBtn()
        time.sleep(0.5)
        self.clickAddUserOptionBtn()
        time.sleep(0.5)

    def inputName(self, first_name, last_name, userName):
        self.inputFirstName(first_name)
        self.inputLastName(last_name)
        self.inputUserName(userName)
    def inputResidentialInfo(self, address, city, postal_code):
        self.clickResidentialAccordionMenu()
        self.inputAddress(address)
        self.inputCity(city)
        self.inputPostalCode(postal_code)

