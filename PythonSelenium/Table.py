import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Program Files\Selenium-driverfiles\chromedriver_win32\chromedriver.exe")
driver.get("https://datatables.net/")
driver.maximize_window()
table_rows_ele = driver.find_elements_by_xpath("//*[@id='example']/tbody/tr")
table_rows_count = len(table_rows_ele)
print("Rows = " + str(table_rows_count))

table_columns_count = len(driver.find_elements_by_xpath("//*[@id='example']/tbody/tr[1]/td"))
print("Columns = " + str(table_columns_count))

for r in range(2, table_rows_count + 1):
    for c in range(1, table_columns_count + 1):
        table_ele = driver.find_element_by_xpath("//*[@id='example']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]")
        print(table_ele.text, end='    ')
    print()
