import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path= "C:\Program Files\Selenium-driverfiles\geckodriver_win_32\geckodriver.exe")
driver.get("https://www.rediff.com/")
print(driver.title)  # Title of the page
print(driver.current_url)  # Returns current url of the page
driver.find_element_by_xpath("//*[@class='logobar']//*[@class='cell alignR toprlinks']//*[@title='Create Rediffmail Account']").click()
time.sleep(3)
user_ele = driver.find_element_by_xpath("//*[@id='tblcrtac']/tbody/tr[3]/td[3]/input")

print(user_ele.is_displayed())
print(user_ele.is_enabled())

user_ele.send_keys("satya sunil")
male_ele = driver.find_element_by_xpath("//*input[@value='m']")
print(male_ele.is_selected())
driver.close()
