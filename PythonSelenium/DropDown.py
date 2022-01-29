import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path = "C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")
driver.get("http://register.rediff.com/register/register.php?FormName=user_details")
country_drp = driver.find_element_by_id("country")
country_drp_element = Select(country_drp)

# Capture all option in dropdown and print
all_options = country_drp_element.options
for option in all_options:
    print(option)

# Count number of dropdowns
print(len(country_drp_element.options))
print(len(all_options))

# Different ways to select dropdown
country_drp_element.select_by_visible_text("Angola")
country_drp_element.select_by_index(2)
country_drp_element.select_by_value("99")
driver.quit()

