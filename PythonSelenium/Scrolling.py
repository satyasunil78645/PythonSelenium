from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

# Scroll down the page by pixel
driver.execute_script("window.scrollBy(0,1500)", "")

# Scroll the the page till the element is visible
india_ele = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[79]/div")
driver.execute_script("arguments[0].scrollIntoView();", india_ele)

# How to scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

