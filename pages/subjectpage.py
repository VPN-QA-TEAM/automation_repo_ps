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

    # LOCATORS - KELAS PAGE
    KELAS_DROPDOWNBTN = '//button[@class="btn workbook-label font-weight-bold dropdown-toggle"]'       # by XPATH

    def namaKelasList (nama_kelas):
        KELASLIST_BTN = '//a[@class="dropdown-item" and .="'+nama_kelas+'"]'      # by XPATH

    MAPELWAJIB_TITLE= '//span[.="Wajib"]'   # by XPATH
    MAPELPILIHAN_TOTAL = '//span[.="Wajib"]/ancestor::div[@class="subject-header"]//li[2]'    # by XPATH

    def mapelCard (nama_mapel):
        MAPELITEM_BTN = '//div[.="'+nama_mapel+'"]/parent::div[@class="subject-card-container col-md-2 col-6 mb-5"]'   # by XPATH

    def mapelCardDropdown (nama_mapel):
        MAPELDROPDOWN_BTN = '//div[.="'+nama_mapel+'"]/parent::div[@class="subject-card-container col-md-2 col-6 mb-5"]//div[@class="card-elipsis mr-2 dropdown"]'   # by XPATH

    MAPELPILIHAN_TITLE= '//span[.="Pilihan"]'   # by XPATH
    MAPELPILIHAN_TOTAL = '//span[.="Pilihan"]/ancestor::div[@class="subject-header"]//li[2]'    # by XPATH


    def threeDotsOnKelas(self, nama_kelas):
        THREEDOTS_BUTTON = '//div[.="'+nama_kelas+'"]/parent::div[@class="card text-center course-card m-0 "]//div[@class="header-icon"]' # by XPATH
        THREEDOTS_BUTTON().click()
        time.sleep(0.5)

    