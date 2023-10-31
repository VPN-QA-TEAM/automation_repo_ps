import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.loginpage import LoginPage


class SubjectPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


########################################## LOCATORS ###########################################################################

    SUBJECT_SIDEBARS_BTN = '//li[@class="menu-item icon-pelajaran"]'  # by XPATH
    SKIPINPUTEMAIL_BTN = '//button[@class="btn btn-skip margin-top"]'  # by XPATH
    TITLE_HEADER = '//div/h3'      # by XPATH
    HIDDENSUBJECT_TOGGLE = '//div[@class="custom-control custom-switch"]'     # by XPATH
    ADDCOURSE_BTN = '//button[.="Tambah Pembelajaran"]'      # by XPATH

    #LOCATORS - TAMBAH & EDIT PEMBELAJARAN MODAL
    MODAL_TITLE = '//h4[@class="modal-title"]'    # by XPATH
    KM_RADIOBTN = '//input[@id="curriculum_type_0"]'    # by XPATH
    K13_RADIOBTN = '//input[@id="curriculum_type_1"]'    # by XPATH
    JENJANGKELAS_DROPDOWNFIELD = '//select[@name="grade"]'     # by XPATH

    def jenjangKelasListOptions(self, jenjang_kelas):  # jenjang_kelas = 7/8/9 (Use String Type)
        JENJANG_KELAS_LIST = '//select[@name="grade"]/option[@value="'+jenjang_kelas+'"]'  # by XPATH
        return JENJANG_KELAS_LIST

    NAMAPEMBELAJARAN_INPUTFIELD = '//input[@name="course_name"]'     # by XPATH
    MAPEL_INPUTFIELD = '//input[@name="searchTerm"]'     # by XPATH
    CANCELADDCOURSE_BTN = '//button[@class="btn btn-cancel"]'     # by XPATH
    DONE_TAMBAHPEMBELAJARAN_BTN = '//button[@type="submit"]'     # by XPATH

    def clickChooseMapel(self, nama_mapel):
        MAPEL_CHECKBOX = '//div/span[.="'+nama_mapel+'"]'      # Locator by XPATH
        MAPEL_CHECKBOX().click()
        time.sleep(0.5)


    # LOCATORS - KELAS CARD


    def kelasCard(self, nama_kelas_card):
        KELAS_CARD_BTN = '//div[.="'+nama_kelas_card+'"]/parent::div[@class="card text-center course-card m-0 "]'  # Locator by XPATH
        return KELAS_CARD_BTN

    # LOCATORS - KELAS PAGE
    CLOSE_FLOATER_BTN = '//button[@data-action="close"]'
    KELAS_DROPDOWNBTN = '//button[@class="btn workbook-label font-weight-bold dropdown-toggle"]'       # by XPATH

    def namaKelasList(self, nama_kelas):
        KELASLIST_BTN = '//a[@class="dropdown-item" and .="'+nama_kelas+'"]'      # by XPATH
        return KELASLIST_BTN

    MAPELWAJIB_TITLE = '//span[.="Wajib"]'   # by XPATH
    MAPELPIWAJIB_TOTAL = '//span[.="Wajib"]/ancestor::div[@class="subject-header"]//li[2]'    # by XPATH

    def mapelCard(self, nama_mapel):
        MAPELITEM_BTN = '//div[.="'+nama_mapel+'"]/parent::div[@class="subject-card-container col-md-2 col-6 mb-5"]'   # by XPATH
        return MAPELITEM_BTN

    def mapelCardDropdown(self, nama_mapel):
        MAPELDROPDOWN_BTN = '//div[.="'+nama_mapel+'"]/parent::div[@class="subject-card-container col-md-2 col-6 mb-5"]//div[@class="card-elipsis mr-2 dropdown"]'   # by XPATH
        return MAPELDROPDOWN_BTN

    def mapelCardDropdownOptionList(self, option_list):  # Option List = Ubah / Hapus
        MAPELDROPDOWN_OPTIONLIST = '//div[@class="p-0 dropdown-menu show"]/button[.="'+option_list+'"]'  # Locators by XPATH
        return MAPELDROPDOWN_OPTIONLIST

    MAPELPILIHAN_TITLE = '//span[.="Pilihan"]'   # by XPATH
    MAPELPILIHAN_TOTAL = '//span[.="Pilihan"]/ancestor::div[@class="subject-header"]//li[2]'    # by XPATH


    def threeDotsOnKelas(self, nama_pembelajaran):
        THREEDOTS_BUTTON = '//div[.="'+nama_pembelajaran+'"]/parent::div//div[@class="header-icon"]'  # by XPATH
        return THREEDOTS_BUTTON

    THREEDOTS_EDIT_OPTION_LIST = '//a[@class="dropdown-item" and .="Ubah" or .="Edit"]'  # by XPATH
    THREEDOTS_DELETE_OPTION_LIST = '//a[@class="dropdown-item" and .="Hapus" or .="Delete"]'  # by XPATH
    THREEDOTS_HIDECOURSE_OPTION_LIST = '//a[@class="dropdown-item" and .="Sembunyikan Kursus" or .="Hide Course"]'  # by XPATH
    THREEDOTS_UNHIDECOURSE_OPTION_LIST = '//a[@class="dropdown-item" and .="Perlihatkan Kursus" or .="Unhide Course"]'  # by XPATH

    DELETECONFIRMATION_YES_BTN = '//button[@class="btn yesDeleteMeeting  "]'  # by XPATH
    DELETECONFIRMATION_NO_BTN = '//button[@class=" btn noDeleteMeeting  "]'  # by XPATH

    TOAST_SUCCESS_DELETE = '//div[@class="Toastify__toast Toastify__toast--default"]'

    # LOCATORS - TAMBAH MATA PELAJARAN
    ADDMAPEL_BTN = '//button[@type="button" and .="Tambah mata pelajaran"]'  # by XPATH
    ADDMAPEL_MODALTITLE = '//h4[@id="modalLabel" and .="Tambah mata pelajaran"]'  # by XPATH
    NAMAMAPEL_INPUTFIELD = '//label[.="Nama Mata Pelajaran"]/parent::div[@class="form-group row noMar"]//input[@type="text"]'  # by XPATH
    NAMAPENDEK_INPUTFIELD = '//label[.="Nama pendek"]/parent::div[@class="col-6 form-group mr-2 mb-0 pl-0"]//input[@type="text"]'  # by XPATH
    WARNATEMA_BTN = '//div[@class="form-control p-4 da-color-palette"]'  # by XPATH

    def chooseColor(self, nomor_posisi):  # Posisi = 1 - 24
        COLOR_BTN = '//div[@class="colorDotContainer "]/div['+nomor_posisi+']/div[@class="colorDot"]'  # Locator by XPATH
        return COLOR_BTN

    def jenisSubjek(self, tipe_subjek):  # Locator by XPATH | tipe_subjek = Wajib/Pilihan
        JENIS_SUBJEK_BTN = '//input[@class="curriculum-input"]/ancestor::div/label[.="'+tipe_subjek+'"]'  # by XPATH
        return JENIS_SUBJEK_BTN

    def mapelIcon(self, nomor_posisi):   # Posisi = 1 - 12
        ICON_BTN = '//label[@class="icon-check"]/ancestor::ul[@class="checking-box"]//li['+nomor_posisi+']'  # Locator by XPATH
        return ICON_BTN

    def mapelBackground(self, nomor_posisi):     # Posisi = 1 - 12
        BG_BTN = '//label[@class="images-check"]/ancestor::ul[@class="checking-box"]//li['+nomor_posisi+']'  # Locator by XPATH
        return BG_BTN

    TERAPKANPEMBELAJARAN_DROPDOWNBTN = '//div[@class="da-multi-select    form-control subject-multi-select"]'  # by XPATH

    def terapkanPembelajaranListOption(self, nama_kelas):
        TERAPKAN_PEMBELAJARAN_LIST = '//input[@type="checkbox"]/ancestor::div//span[.="'+nama_kelas+'"]'  # by XPATH
        return TERAPKAN_PEMBELAJARAN_LIST

    def threeDotsOnMapelCard(self, nama_mapel):
        THREEDOTS_MAPEL_BTN = '//div[@class="subject-name" and .="'+nama_mapel+'"]/parent::div//div[@class="card-elipsis mr-2 dropdown"]'
        return THREEDOTS_MAPEL_BTN

    def threeDotsListOptionOnMapelCard(self, nama_action):
        THREEDOTS_LIST_OPTION = '//button[.="'+nama_action+'"]'
        return THREEDOTS_LIST_OPTION

    EDIT_MAPEL_THREEDOTS_LIST_BTN = '//button[.="Edit" or .="Ubah"]'
    DELETE_MAPEL_THREEDOTS_LIST_BTN = '//button[.="Delete" or .="Hapus"]'

    SAVE_MAPEL_BTN = '//button[@class="btn btn-lg btn-primary"]'  # by XPATH
    CANCEL_ADDMAPEL_BTN = '//button[@class="btn btn-lg btn-cancel"]'  # by XPATH


    # LOCATORS - MATA PELAJARAN PAGE

    MAPEL_DROPDOWN_BTN = '//span[@id="dropdownMenuLink"]'  # by XPATH

    def mapelDropdownListOptionButton(self, nama_mapel):
        MAPEL_DROPDOWN_LIST_OPTION = '//div[@class="dropdown-menu subject-list show"]//div//span[.="'+nama_mapel+'"]'  # by XPATH
        return MAPEL_DROPDOWN_LIST_OPTION

    SEMESTER1_TOGLE_SWITCH = '//ul[@class="btn-switch mb-0"]/li[1]'  # by XPATH
    SEMESTER2_TOGLE_SWITCH = '//ul[@class="btn-switch mb-0"]/li[2]'  # by XPATH
    TAMBAHBAB_BTN = '//button[contains(.,"Tambah Bab")]'  # by XPATH
    UNGGAHBUKU_BTN = '//button[.="Unggah buku"]'  # by XPATH

    def babDropDownBtn(self, nama_bab):
        BAB_DROPDOWN_BTN = '//span[.="'+nama_bab+'"]/ancestor::div[@class="row noMar align-items-center mb-0"]//button[@class="btn btn-link p-2 text-left"]'  # by XPATH
        return BAB_DROPDOWN_BTN

    def babAddTopicBtn(self, nama_bab):
        BAB_ADDTOPIC_BTN = '//span[.="'+nama_bab+'"]/ancestor::div[@class="row noMar align-items-center mb-0"]//button[@class="btn btn-link"]'  # by XPATH
        return BAB_ADDTOPIC_BTN


    # LOCATORS - TAMBAH BAB MODAL

    NOMORBAB_FIELD = '//input[@name="chapter_number"]'  # by XPATH
    NAMABAB_FIELD = '//input[@name="chapter_name"]'  # by XPATH
    SEMESTER_DROPDOWN_FIELD = '//select[@name="semester"]'  # by XPATH

    def semesterDropdownListOption(self, semester):  # SEMESTER = 1 / 2
        SEMESTER_DROPDOWN_LIST_OPTION = '//select[@name="semester"]//option[@value="'+semester+'"]'
        return SEMESTER_DROPDOWN_LIST_OPTION

    TIDAKTERBITKAN_TOGGLE_SWITCH = '//label[@class="toggle-switch"]'  # Default = Terbitkan. Click Once for Tidak Terbitkan
    BATAL_TAMBAHBAB_BTN = '//button[@class="btn btn-lg btn-cancel"]'  # # by XPATH
    SELESAI_TAMBAHBAB_BTN = '//button[@class="btn btn-lg btn-primary"]'  # by XPATH


    # LOCATORS - TAMBAH TOPIC MODAL

    INDENTASI_DROPDOWN_FIELD = '//select[@id="topic-indent"]'  # by XPATH

    def indentasiLevelDropdownListOption(self, indentasi_level):  # Indentasi Level = 1 / 2
        INDENTASI_DROPDOWN_LIST_OPTION = '//select[@id="topic-indent"]/parent::div[@class="col"]//option[@value="'+indentasi_level+'"]'  # by XPATH
        return INDENTASI_DROPDOWN_LIST_OPTION

    INDENTASI1_FIELD = '//input[@name="indent1"]'  # by XPATH
    INDENTASI2_FIELD = '//input[@name="indent2"]'  # by XPATH (Only available when choose Indentasi Level 2)
    NAMATOPIK_FIELD = '//input[@name="topic_name"]'  # by XPATH
    BATAL_TAMBAHTOPIC_BTN = '//button[@class="btn btn-lg btn-cancel"]'  # by XPATH
    SELESAI_TAMBAHTOPIC_BTN = '//button[@class="btn btn-lg btn-primary"]'  # by XPATH

    


################################################################# ACTION ###########################################################################


    def getSkipEmailBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.SKIPINPUTEMAIL_BTN)

    def getSubjectSidebarsBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.SUBJECT_SIDEBARS_BTN)

    def getSubjectTitleHeader(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.TITLE_HEADER)

    def getCloseFloaterBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.CLOSE_FLOATER_BTN)

    def getTambahPembelajaranBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.ADDCOURSE_BTN)

    def getKelasCard(self, nama_kelas_card):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.kelasCard(nama_kelas_card))

    def getKelasTitle(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.KELAS_DROPDOWNBTN)

    def getModalTitle(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.MODAL_TITLE)

    def getKurikulumK13Btn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.K13_RADIOBTN)

    def getJenjangKelasField(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.JENJANGKELAS_DROPDOWNFIELD)

    def getJenjangKelasListOptions(self, jenjang_kelas):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.jenjangKelasListOptions(jenjang_kelas))

    def getNamaPembelajaranField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.NAMAPEMBELAJARAN_INPUTFIELD)

    def getDoneTambahPembelajaranBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.DONE_TAMBAHPEMBELAJARAN_BTN)

    ################ Three Dots Actions #################
    def getThreeDotsBtn(self, nama_pembelajaran):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.threeDotsOnKelas(nama_pembelajaran))

    def getThreeDotsEditOptionBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.THREEDOTS_EDIT_OPTION_LIST)

    def getThreeDotsDeleteOptionBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.THREEDOTS_DELETE_OPTION_LIST)

    def getThreeDotsHideCourseOptionBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.THREEDOTS_HIDECOURSE_OPTION_LIST)

    def getThreeDotsUnhideCourseOptionBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.THREEDOTS_UNHIDECOURSE_OPTION_LIST)

    ########################################################

    def getDeleteConfrimationYesBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.DELETECONFIRMATION_YES_BTN)

    def getDeleteConfrimationNoBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.DELETECONFIRMATION_NO_BTN)

    def getSuccessDeleteToast(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.TOAST_SUCCESS_DELETE)

    def getShowHiddenSubjectToggle(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.HIDDENSUBJECT_TOGGLE)

    def getAddMapelBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.ADDMAPEL_BTN)

    def getNamaMapelInputField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.NAMAMAPEL_INPUTFIELD)

    def getNamaPendekMapelInputField(self):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.NAMAPENDEK_INPUTFIELD)

    def getChooseColorField(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.WARNATEMA_BTN)

    def getColorButton(self, nomor_posisi):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.chooseColor(nomor_posisi))

    def getJeniSubjekRadioBtn(self, tipe_subjek):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.jenisSubjek(tipe_subjek))

    def getMapelIconBtn(self, nomor_posisi):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.mapelIcon(nomor_posisi))

    def getMapelBackgroundBtn(self, nomor_posisi):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.mapelBackground(nomor_posisi))

    def getSaveAddMapelBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.SAVE_MAPEL_BTN)

    def getCancelAddMapelBtn(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.CANCEL_ADDMAPEL_BTN)

    def getMapelCard(self, nama_mapel):
        return self.wait15sec_until_element_is_presence(By.XPATH, self.mapelCard(nama_mapel))

    def getTerapkanPembelajaranDropdownField(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.TERAPKANPEMBELAJARAN_DROPDOWNBTN)

    def getTerapkanPembelajaranListOptions(self, nama_kelas):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.terapkanPembelajaranListOption(nama_kelas))

    def getThreeDotsOnMapelCard(self, nama_mapel):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.threeDotsOnMapelCard(nama_mapel))

    def getThreedotsEditOptionOnMapelCard(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.EDIT_MAPEL_THREEDOTS_LIST_BTN)

    def getThreedotsDeleteOptionOnMapelCard(self):
        return self.wait15sec_until_element_is_clickable(By.XPATH, self.DELETE_MAPEL_THREEDOTS_LIST_BTN)






    def goToSubjectPage(self, inputUserId, inputPassword):
        login = LoginPage(self.driver)
        login.userLogin(inputUserId, inputPassword)
        time.sleep(1.0)
        self.clickSkipEmailBtn()
        time.sleep(0.5)
        self.clickSubjectSidebarsBtn()
        time.sleep(0.5)
        self.clickCloseFloaterBtn()
        time.sleep(0.5)
        self.verifySubjectPage()
        time.sleep(0.5)


    def clickSkipEmailBtn(self):
        self.getSkipEmailBtn().click()

    def clickSubjectSidebarsBtn(self):
        self.getSubjectSidebarsBtn().click()
        time.sleep(0.5)

    def verifySubjectPage(self):
        self.getSubjectTitleHeader().is_displayed()
        time.sleep(1.0)

    def clickCloseFloaterBtn(self):
        self.getCloseFloaterBtn().click()
        time.sleep(1.0)

    def clickTambahPembelajaranBtn(self):
        self.getTambahPembelajaranBtn().click()
        time.sleep(0.5)

    def clickKelasCard(self, nama_kelas_card):
        self.getKelasCard(nama_kelas_card).click()
        time.sleep(1.0)

    def verifyKelasPage(self, kelas_title):
        validation_msg = self.getKelasTitle().text
        time.sleep(1.0)
        assert validation_msg == kelas_title
        time.sleep(1.0)

    def verifyTambahPembelajaranModalTitle(self):
        self.getModalTitle().is_displayed()
        time.sleep(1.0)

    def clickKurikulumK13Btn(self):
        self.getKurikulumK13Btn().click()
        time.sleep(0.5)

    def clickJenjangKelasField(self):
        self.getJenjangKelasField().click()
        time.sleep(0.5)

    def clickJenjangKelasListOption(self, jenjang_kelas):
        self.getJenjangKelasListOptions(jenjang_kelas).click()
        time.sleep(0.3)

    def inputNamaPembelajaran(self, nama_pembelajaran):
        self.getNamaPembelajaranField().clear()
        self.getNamaPembelajaranField().send_keys(nama_pembelajaran)
        time.sleep(0.5)

    def clickDoneTambahPembelajaranBtn(self):
        self.getDoneTambahPembelajaranBtn().click()
        time.sleep(0.5)

    ################ Three Dots Actions #################
    def clickThreeDotsOnKelas(self, nama_pembelajaran):
        self.getThreeDotsBtn(nama_pembelajaran).click()
        time.sleep(0.5)

    def clickThreeDotsEditBtn(self):
        self.getThreeDotsEditOptionBtn().click()
        time.sleep(0.5)

    def clickThreeDotsDeleteBtn(self):
        self.getThreeDotsDeleteOptionBtn().click()
        time.sleep(0.5)

    def clickThreeDotsHideCourseBtn(self):
        self.getThreeDotsHideCourseOptionBtn().click()
        time.sleep(0.5)

    def clickThreeDotsUnhideCourseBtn(self):
        self.getThreeDotsUnhideCourseOptionBtn().click()
        time.sleep(0.5)

    ########################################################

    def clickDeleteConfirmationYesBtn(self):
        self.getDeleteConfrimationYesBtn().click()
        time.sleep(0.3)

    def clickDeleteConfirmationNoBtn(self):
        self.getDeleteConfrimationNoBtn().click()
        time.sleep(0.5)

    def verifySuccessDelete(self):
        self.getSuccessDeleteToast().is_displayed()
        time.sleep(0.5)

    def clickShowHiddenSubjectToggle(self):
        self.getShowHiddenSubjectToggle().click()
        time.sleep(0.5)

    def verifyAddNewKelas(self, nama_kelas_card):
        self.getKelasCard(nama_kelas_card).is_displayed()

    def clickAddMapelBtn(self):
        self.getAddMapelBtn().click()
        time.sleep(0.5)

    def inputNamaMapel(self, nama_mapel):
        self.getNamaMapelInputField().clear()
        time.sleep(0.1)
        self.getNamaMapelInputField().send_keys(nama_mapel)
        time.sleep(0.5)

    def inputNamaPendekMapel(self, nama_pendek_mapel):
        self.getNamaPendekMapelInputField().clear()
        time.sleep(0.1)
        self.getNamaPendekMapelInputField().send_keys(nama_pendek_mapel)
        time.sleep(0.5)

    def clickChooseColorField(self):
        self.getChooseColorField().click()
        time.sleep(0.5)

    def clickColorBtn(self, nomor_posisi):
        self.getColorButton(nomor_posisi).click()
        time.sleep(0.5)

    def clickTipeSubjekRadioBtn(self, tipe_subjek):
        self.getJeniSubjekRadioBtn(tipe_subjek).click()
        time.sleep(0.5)

    def clickMapelIconBtn(self, nomor_posisi):
        self.getMapelIconBtn(nomor_posisi).click()
        time.sleep(1.0)

    def clickMapelBackgroundBtn(self, nomor_posisi):
        self.getMapelBackgroundBtn(nomor_posisi).click()
        time.sleep(0.5)

    def clickSaveAddMapelBtn(self):
        self.getSaveAddMapelBtn().click()
        time.sleep(0.5)

    def clickCancelAddMapelBtn(self):
        self.getCancelAddMapelBtn().click()
        time.sleep(0.5)

    def verifyAddMapel(self, nama_kelas_card):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(self.getMapelCard(nama_kelas_card))
        time.sleep(0.2)
        self.getMapelCard(nama_kelas_card).is_displayed()
        time.sleep(1.0)

    def clickTerapkanPembelajaranField(self):
        self.getTerapkanPembelajaranDropdownField().click()
        time.sleep(0.5)

    def clickTerapkanPembelajaranListOptionBtn(self, nama_kelas):
        self.getTerapkanPembelajaranListOptions(nama_kelas).click()
        time.sleep(0.5)

    def clickMapelCard(self, nama_kelas_card):
        actions = ActionChains(self.driver)
        actions.scroll_to_element(self.getMapelCard(nama_kelas_card))
        time.sleep(0.2)
        self.getMapelCard(nama_kelas_card).click()
        time.sleep(0.5)

    def clickThreeDotsOnMapelCard(self, nama_mapel):
        self.getThreeDotsOnMapelCard(nama_mapel).click()
        time.sleep(1.0)

    def clickThreeDotsEditMapelListOption(self):
        self.getThreedotsEditOptionOnMapelCard().click()
        time.sleep(0.5)

    def clickThreeDotsDeleteMapelListOption(self):
        self.getThreedotsDeleteOptionOnMapelCard().click()
        time.sleep(0.5)