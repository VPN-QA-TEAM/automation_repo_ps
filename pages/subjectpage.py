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
    CANCELADDCOURSE_BTN = '//button[@class="btn btn-cancel"]'     # by XPATH
    DONE_BTN = '//button[@type="submit"]'     # by XPATH

    def clickChooseMapel(self, nama_mapel):
        MAPEL_CHECKBOX = '//div/span[.="'+nama_mapel+'"]'      # Locator by XPATH
        MAPEL_CHECKBOX().click()
        time.sleep(0.5)

    # LOCATORS - KELAS CARD
    def clickKelasButton(self, nama_kelas):
        KELAS_BTN = '//div[.="'+nama_kelas+'"]'      # Locator by XPATH
        KELAS_BTN().click()
        time.sleep(0.5)

    # LOCATORS - KELAS PAGE
    KELAS_DROPDOWNBTN = '//button[@class="btn workbook-label font-weight-bold dropdown-toggle"]'       # by XPATH

    def namaKelasList (self, nama_kelas):
        KELASLIST_BTN = '//a[@class="dropdown-item" and .="'+nama_kelas+'"]'      # by XPATH

    MAPELWAJIB_TITLE= '//span[.="Wajib"]'   # by XPATH
    MAPELPILIHAN_TOTAL = '//span[.="Wajib"]/ancestor::div[@class="subject-header"]//li[2]'    # by XPATH

    def mapelCard (self, nama_mapel):
        MAPELITEM_BTN = '//div[.="'+nama_mapel+'"]/parent::div[@class="subject-card-container col-md-2 col-6 mb-5"]'   # by XPATH

    def mapelCardDropdown (self, nama_mapel):
        MAPELDROPDOWN_BTN = '//div[.="'+nama_mapel+'"]/parent::div[@class="subject-card-container col-md-2 col-6 mb-5"]//div[@class="card-elipsis mr-2 dropdown"]'   # by XPATH

    def mapelCardDropdownOptionList (self, option_list): # Option List = Ubah / Hapus
        MAPELDROPDOWN_OPTIONLIST = '//div[@class="p-0 dropdown-menu show"]/button[.="'+option_list+'"]'  # Locators by XPATH

    MAPELPILIHAN_TITLE= '//span[.="Pilihan"]'   # by XPATH
    MAPELPILIHAN_TOTAL = '//span[.="Pilihan"]/ancestor::div[@class="subject-header"]//li[2]'    # by XPATH


    def threeDotsOnKelas(self, nama_kelas):
        THREEDOTS_BUTTON = '//div[.="'+nama_kelas+'"]/parent::div[@class="card text-center course-card m-0 "]//div[@class="header-icon"]' # by XPATH
        THREEDOTS_BUTTON().click()
        time.sleep(0.5)

    # LOCATORS - TAMBAH MATA PELAJARAN
    ADDMAPEL_BTN = '//button[@type="button" and .="Tambah mata pelajaran"]' # by XPATH
    ADDMAPEL_MODALTITLE = '//h4[@id="modalLabel" and .="Tambah mata pelajaran"]' # by XPATH
    NAMAMAPEL_INPUTFIELD = '//label[.="Nama Mata Pelajaran"]/parent::div[@class="form-group row noMar"]//input[@type="text"]' # by XPATH
    NAMAPENDEK_INPUTFIELD = '//label[.="Nama pendek"]/parent::div[@class="col-6 form-group mr-2 mb-0 pl-0"]//input[@type="text"]' # by XPATH
    WARNATEMA_BTN = '//div[@class="form-control p-4 da-color-palette"]' # by XPATH

    def chooseColor (self, nomor_posisi):  # Locator by XPATH
        COLOR_BTN = '//div[@class="colorDotContainer"]/div['+nomor_posisi+']' 

    def jenisSubjek (self, tipe_subjek): # Locator by XPATH | tipe_subjek = Wajib/Pilihan
        JENISSUBJEK_BTN = '//input[@class="curriculum-input"]/ancestor::div/label[.="'+tipe_subjek+'"]' # by XPATH

    def mapelIcon (self, nomor_posisi):   # Locator by XPATH
        ICON_BTN = '//label[@class="icon-check"]/ancestor::ul[@class="checking-box"]//li['+nomor_posisi+']'     

    def mabelBackground (self, nomor_posisi) :     # Locator by XPATH
        BG_BTN = '//label[@class="images-check"]/ancestor::ul[@class="checking-box"]//li['+nomor_posisi+']'

    TERAPKANPEMBELAJARAN_DROPDOWNBTN = '//div[@class="da-multi-select    form-control subject-multi-select"]' # by XPATH

    def terapkanPembelajaranListOption (self, nama_kelas):
        TERAPKANPEMBELAJARAN_LIST = '//input[@type="checkbox"]/ancestor::div//span[.="'+nama_kelas+'"]' # by XPATH

    SAVEMAPEL_BTN = '//button[@class="btn btn-lg btn-primary"]' # by XPATH
    CANCELADDMAPEL_BTN = '//button[@class="btn btn-lg btn-cancel"]' # by XPATH


    # LOCATORS - MATA PELAJARAN PAGE
    MAPEL_DROPDOWN_BTN = '//span[@id="dropdownMenuLink"]' # by XPATH

    def mapelDropdownListOptionButton (self, nama_mapel) :
        MAPEL_DROPDOWN_LIST_OPTION = '//div[@class="dropdown-menu subject-list show"]//div//span[.="'+nama_mapel+'"]' # by XPATH

    SEMESTER1_TOGLE_SWITCH = '//ul[@class="btn-switch mb-0"]/li[1]' # by XPATH
    SEMESTER2_TOGLE_SWITCH = '//ul[@class="btn-switch mb-0"]/li[2]' # by XPATH
    TAMBAHBAB_BTN = '//button[contains(.,"Tambah Bab")]' # by XPATH
    UNGGAHBUKU_BTN = '//button[.="Unggah buku"]' # by XPATH