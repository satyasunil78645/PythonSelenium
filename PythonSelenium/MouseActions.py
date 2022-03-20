from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# platform_menu_ele = driver.find_element_by_xpath("//*[@id='header-navbar']/ul[1]/li[1]/a")
# Hr_admin_ele = driver.find_element_by_xpath("//*[@id='header-navbar']/ul[1]/li[1]/div/div[1]/div[1]/div/div[1]/p[1]/a")
#
# # Mouse hover actions
actions = ActionChains(driver)
# actions.move_to_element(platform_menu_ele).move_to_element(Hr_admin_ele).click().perform()

# double click actions
driver.get("https://testautomationpractice.blogspot.com/")
double_ele = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions.double_click(double_ele).perform()
print("Mouse actions")
