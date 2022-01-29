from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")

driver.get("https://www.rediff.com/")

driver.implicitly_wait(10)  # Implicit wait applicable to all elements (10) sec
assert "Rediff.com: News | Rediffmail | Stock Quotes | Shopping" in driver.title


