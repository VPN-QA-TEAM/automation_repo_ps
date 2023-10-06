import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class SubjectPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


########################################## LOCATORS ###########################################################################
    
    TITLE_HEADER = '//div/h3'      # by XPATH
    HIDDENSUBJECT_TOGLE = '//div/input[@id="customSwitch-1"]'     # by XPATH
    ADDCOURSE_BTN = '//button[.="Tambah Pembelajaran"]'      # by XPATH

    #LOCATORS - ADD COURSE MODAL
    MODAL_TITLE = '//h4[@class="modal-title"]'    # by XPATH
    KM_RADIOBTN = '//input[@id="curriculum_type_0"]'    # by XPATH
    K13_RADIOBTN = '//input[@id="curriculum_type_1"]'    # by XPATH
    GRADE_DROPDOWNFIELD = '//select[@name="grade"]'     # by XPATH
    GRADE7_LISTOPTION = '//select[@name="grade"]/option[@value="7"]'     # by XPATH
    GRADE8_LISTOPTION = '//select[@name="grade"]/option[@value="8"]'     # by XPATH
    GRADE9_LISTOPTION = '//select[@name="grade"]/option[@value="9"]'     # by XPATH
    JURUSAN_INPUTFIELD = '//input[@name="course_name"]'     # by XPATH 
    MAPEL_INPUTFIELD = '//input[@name="searchTerm"]'     # by XPATH
    CANCEL_BTN = '//button[@class="btn btn-cancel"]'     # by XPATH
    DONE_BTN = '//button[@type="submit"]'     # by XPATH

    def clickChooseMapel(self, nama_mapel):
        MAPEL_CHECKBOX = '//div/span[.="'+nama_mapel+'"]]'      # Locator by XPATH
        MAPEL_CHECKBOX().click()
        time.sleep(0.5)

    # LOCATORS - KELAS CARD

    def clickKelasButton(self, nama_kelas):
        KELAS_BTN = '//div[.="'+nama_kelas+'"]'      # Locator by XPATH
        KELAS_BTN().click()
        time.sleep(0.5)

    def threeDotsOnKelas(self, nama_kelas):
        THREEDOTS_BUTTON = '//div[.="'+nama_kelas+'"]/parent::div[@class="card text-center course-card m-0 "]//div[@class="header-icon"]' # by XPATH
        THREEDOTS_BUTTON().click()
        time.sleep(0.5)

    