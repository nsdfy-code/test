import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

element = driver.find_element(By.ID,"userA")

element.send_keys("admin1")

time.sleep(3)

element.send_keys(Keys.BACKSPACE)

time.sleep(3)

element.send_keys(Keys.CONTROL,"a")

time.sleep(3)

element.send_keys(Keys.CONTROL,"c")

element2=driver.find_element(By.ID,"telA")

time.sleep(3)

# element2.click()

time.sleep(3)

element2.send_keys(Keys.CONTROL,"v")

time.sleep(3)

driver.quit()