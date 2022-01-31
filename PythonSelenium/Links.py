import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")

driver.get("https://www.rediff.com/")
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME, 'a')

print("Total number of Links in a page", len(links))

driver.find_element(By.LINK_TEXT, 'Sign in').click()
for link in links:
    print(link.text)

