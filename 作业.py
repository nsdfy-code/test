import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.jd.com")

time.sleep(5)

driver.quit()