import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://baidu.com")

time.sleep(3)

driver.quit()