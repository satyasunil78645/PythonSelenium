import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://techcanvass.com/examples/register.html")
driver.implicitly_wait(10)

female_status = driver.find_element_by_xpath("//*[@id='login']//input[@type='radio' and @value='female']").is_selected()
male_status = driver.find_element_by_xpath("//*[@id='login']//input[@type='radio' and @value='male']").is_selected()
print(male_status)
print(female_status)
driver.find_element_by_xpath("//*[@id='login']//input[@type='radio' and @value='female']").click()
print(female_status)
checkbox = driver.find_element_by_xpath("//*[@type='checkbox']")
print(checkbox.is_selected())
checkbox.click()
print(checkbox.is_selected())



