import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")

driver.get("https://www.rediff.com/")

print(driver.title)  # Title of the page

print(driver.current_url)  # Returns current url of the page
driver.find_element_by_xpath("//*[@data-tabno='1' and text() = 'LATEST']").click()
time.sleep(5)
print("satya sunil")
driver.close()