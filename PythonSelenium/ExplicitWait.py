import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.co.in/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("(//*[@id='uitk-tabs-button-container']//li)[2]").click()
time.sleep(2)  # python

driver.find_element(By.ID,"location-field-leg1-origin-menu").click()
driver.find_element_by_xpath("//*[@data-stid='location-field-leg1-origin-menu-input']").send_keys("New York, NY, United States of America (JFK)")
time.sleep(3)
driver.find_element_by_xpath("(//*[@data-stid='location-field-leg1-origin-results']//li)[1]").click()

driver.find_element(By.ID,"location-field-leg1-destination-menu").click()
driver.find_element_by_xpath("//*[@data-stid='location-field-leg1-destination-menu-input']").send_keys("Tokyo, Japan (TYO)")
time.sleep(3)
driver.find_element_by_xpath("(//*[@data-stid='location-field-leg1-destination-results']//li)[1]").click()
driver.find_element_by_xpath("//*[@data-testid='submit-button']").click()
# Explicit wait - It's not on the time base. we use this for conditions base

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='changeOptionFilter-0']")))
element.click()


