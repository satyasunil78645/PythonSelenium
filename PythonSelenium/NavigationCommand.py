from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path= "C:\Program Files\Selenium-driverfiles\geckodriver_win_32\geckodriver.exe")

driver.get("https://www.rediff.com/")  # --> Rediff mail
print(driver.title)  # Title of the page

driver.get("https://www.amazon.in/")   # --> Amazon
print(driver.title)  # Title of the page

driver.back()
print(driver.title)  # Title of the page  # --> Rediff mail

driver.forward()
print(driver.title)  # Title of the page  # --> Amazon\

driver.close()
