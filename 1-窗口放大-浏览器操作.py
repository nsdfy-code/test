import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

time.sleep(5)

driver.maximize_window()

time.sleep(5)

driver.quit()