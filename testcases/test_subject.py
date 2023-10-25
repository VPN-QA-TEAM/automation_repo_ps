import pytest

from pages.subjectpage import SubjectPage

NAMA_KELAS = 'Kelas 7'
NAMA_PEMBELAJARAN = 'Test Automation'
NAMA_ADD_MAPEL = 'Mapel Automation'
NAMA_PENDEK_ADD_MAPEL = 'MAT'


@pytest.mark.usefixtures("setup")
class TestSubject:
    """-------------------------------------SCENARIO SUBJECT--------------------------------------------"""
    ##### SUBJECT PAGE #####

    def test_create_new_kelas(self):
        subject = SubjectPage(self.driver)
        subject.goToSubjectPage("admin.uat", "password123*")
        subject.clickTambahPembelajaranBtn()
        subject.verifyTambahPembelajaranModalTitle()
        subject.clickKurikulumK13Btn()
        subject.clickJenjangKelasField()
        subject.clickJenjangKelasListOption("7")
        subject.inputNamaPembelajaran(NAMA_PEMBELAJARAN)
        subject.clickDoneTambahPembelajaranBtn()
        subject.verifyAddNewKelas(NAMA_PEMBELAJARAN)
    #
    # def test_edit_kelas_card(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickThreeDotsOnKelas(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsEditBtn()
    #     subject.inputNamaPembelajaran("Test Edit Nama")
    #     subject.clickDoneTambahPembelajaranBtn()
    #     subject.clickThreeDotsOnKelas("Test Edit Nama")
    #     subject.clickThreeDotsEditBtn()
    #     subject.inputNamaPembelajaran(NAMA_PEMBELAJARAN)
    #     subject.clickDoneTambahPembelajaranBtn()
    #
    # def test_show_hidden_course(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickShowHiddenSubjectToggle()  # Show hidden subject
    #     subject.clickShowHiddenSubjectToggle()  # Hide hidden subject
    #
    # def test_hide_subject(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickThreeDotsOnKelas(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsHideCourseBtn()
    #     subject.clickDeleteConfirmationYesBtn()
    #
    # def test_unhide_hidden_subject(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickShowHiddenSubjectToggle()
    #     subject.clickThreeDotsOnKelas(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsUnhideCourseBtn()

    # def test_delete_kelas_card(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickThreeDotsOnKelas(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsDeleteBtn()
    #     subject.clickDeleteConfirmationYesBtn()
    #     subject.verifySuccessDelete()

    ##### CHOOSE MAPEL PAGE #####

    # def test_create_mapel_pilihan(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickKelasCard(NAMA_PEMBELAJARAN)
    #     subject.verifyKelasPage(NAMA_PEMBELAJARAN)
    #     subject.clickAddMapelBtn()
    #     subject.inputNamaMapel(NAMA_ADD_MAPEL)
    #     subject.inputNamaPendekMapel(NAMA_PENDEK_ADD_MAPEL)
    #     subject.clickChooseColorField()
    #     subject.clickColorBtn('18')  # Posisi = 1 - 24
    #     subject.clickTipeSubjekRadioBtn('Pilihan')  # Tipe Subjek = Wajib / Pilihan
    #     subject.clickMapelIconBtn('6')  # Posisi = 1 - 12
    #     subject.clickMapelBackgroundBtn('8')  # Posisi = 1 - 12
    #     subject.clickSaveAddMapelBtn()
    #     subject.verifyAddMapel(NAMA_ADD_MAPEL)

    # def test_create_mapel_wajib(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickKelasCard(NAMA_PEMBELAJARAN)
    #     subject.verifyKelasPage(NAMA_PEMBELAJARAN)
    #     subject.clickAddMapelBtn()
    #     subject.inputNamaMapel(NAMA_ADD_MAPEL+' Wajib')
    #     subject.inputNamaPendekMapel(NAMA_PENDEK_ADD_MAPEL)
    #     subject.clickChooseColorField()
    #     subject.clickColorBtn('18')  # Posisi = 1 - 24
    #     subject.clickTipeSubjekRadioBtn('Wajib')  # Tipe Subjek = Wajib / Pilihan
    #     subject.clickTerapkanPembelajaranField()
    #     subject.clickTerapkanPembelajaranListOptionBtn('Semua Kelas')  # Semua Kelas / Nama Kelas Tertentu
    #     subject.clickMapelIconBtn('6')  # Posisi = 1 - 12
    #     subject.clickMapelBackgroundBtn('8')  # Posisi = 1 - 12
    #     subject.clickSaveAddMapelBtn()
    #     subject.verifyAddMapel(NAMA_ADD_MAPEL)

    # def test_edit_mapel(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickKelasCard(NAMA_PEMBELAJARAN)
    #     subject.verifyKelasPage(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsOnMapelCard(NAMA_ADD_MAPEL)
    #     subject.clickThreeDotsEditMapelListOption()
    #     subject.inputNamaMapel(NAMA_ADD_MAPEL+' EDIT')
    #     subject.inputNamaPendekMapel(NAMA_PENDEK_ADD_MAPEL+' EDIT')
    #     subject.clickChooseColorField()
    #     subject.clickColorBtn('22')  # Posisi = 1 - 24
    #     subject.clickMapelIconBtn('9')  # Posisi = 1 - 12
    #     subject.clickMapelBackgroundBtn('5')  # Posisi = 1 - 12
    #     subject.clickSaveAddMapelBtn()
    #     subject.verifyAddMapel(NAMA_ADD_MAPEL+' EDIT')
    #     subject.clickThreeDotsOnMapelCard(NAMA_ADD_MAPEL+' EDIT')
    #     subject.clickThreeDotsEditMapelListOption()
    #     subject.inputNamaMapel(NAMA_ADD_MAPEL)
    #     subject.inputNamaPendekMapel(NAMA_PENDEK_ADD_MAPEL)
    #     subject.clickSaveAddMapelBtn()
    #     subject.verifyAddMapel(NAMA_ADD_MAPEL)

    # def test_delete_mapel(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickKelasCard(NAMA_PEMBELAJARAN)
    #     subject.verifyKelasPage(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsOnMapelCard(NAMA_ADD_MAPEL)
    #     subject.clickThreeDotsDeleteMapelListOption()
    #     subject.clickDeleteConfirmationYesBtn()
    #     subject.verifySuccessDelete()

    ##### CLASS PAGE #####
    def test_go_to_mapel_page(self):
        subject = SubjectPage(self.driver)
        subject.goToSubjectPage("admin.uat", "password123*")
        subject.clickKelasCard(NAMA_PEMBELAJARAN)
        subject.verifyKelasPage(NAMA_PEMBELAJARAN)
        subject.clickMapelCard('Bahasa Inggris')
