import pytest

from pages.subjectpage import SubjectPage

NAMA_KELAS = 'Kelas 7'
NAMA_PEMBELAJARAN = 'Test Automation'


@pytest.mark.usefixtures("setup")
class TestSubject:
    """-------------------------------------SCENARIO SUBJECT--------------------------------------------"""
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
    #
    # def test_delete_kelas_card(self):
    #     subject = SubjectPage(self.driver)
    #     subject.goToSubjectPage("admin.uat", "password123*")
    #     subject.clickThreeDotsOnKelas(NAMA_PEMBELAJARAN)
    #     subject.clickThreeDotsDeleteBtn()
    #     subject.clickDeleteConfirmationYesBtn()
    #     subject.verifySuccessDelete()
