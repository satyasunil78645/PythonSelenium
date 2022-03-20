from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")

driver.get("https://www.toysrus.com/")
print("Window name " + driver.current_window_handle) # CDwindow-28F4591D4E2D34FF0313C193EDEFA98D

essential_element = driver.find_element_by_xpath("//*[@class='menu-group']//*[@id='essential-accessibility']")
essential_element.click()

handles = driver.window_handles  # return all the handle values of opened browser windows
print(handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Toysrus.com, The Official Toys”R”Us Site - Toys, Games, & More":
        driver.close()
    else:
        print("Issue")


