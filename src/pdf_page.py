import time
from automationpdfmu.Utilities import utilities

automationpdfmu.Utilities.utilities.init()


def click_upload():
    utilities.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[4]/div[3]/input").send_keys(
        "C:/Users/julea/PycharmProjects/automationpdf/prueba.pdf")


def click_compress():
    utilities.driver.find_element_by_id("processTask").click()
    time.sleep(5)


def validation_name_file():
    return utilities.driver.find_element_by_class_name("file__info__name").text


def validacion_compress():
    return utilities.driver.find_element_by_id("pickfiles").text


def dowload_pdf():
    utilities.driver.find_element_by_id("pickfiles").click()
