import unittest
from automationpdfmu.src import pdf_page
from automationpdfmu.Utilities import utilities


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = utilities
        self.pdf = pdf_page

    def test_upload_file(self):
        self.pdf.click_upload()
        self.assertEqual(self.pdf.validation_name_file(), "prueba.pdf")
        self.pdf.click_compress()
        self.assertEqual(self.pdf.validacion_compress(), "Descargar el PDF optimizado")
        self.pdf.dowload_pdf()

    def tearDown(self):
        self.driver.close()
        if __name__ == '__main__':
            unittest.main()
