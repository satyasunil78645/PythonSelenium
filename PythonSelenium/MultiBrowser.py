from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path = "C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")

driver = webdriver.Firefox(executable_path= "C:\Program Files\Selenium-driverfiles\geckodriver_win_32\geckodriver.exe")

driver.get("https://www.mercurytravels.co.in/")

print(driver.title)  # Title of the page

print(driver.current_url)  # Returns current url of the page

# print(driver.page_source)  # Return the html of the code

driver.close()  # close the browser

