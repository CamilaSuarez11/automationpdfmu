import sys
from selenium import webdriver

print (sys.path[1])
ruth="/chromedriver.exe"
system=sys.path[1]
path=system+ruth
print(path)
driver=None

def init():
    global driver
    driver=webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://www.ilovepdf.com/es/comprimir_pdf")

def close():
    global driver
    driver.quit()

def sendKeys(variable):
    driver.find_element_by_id(variable).send