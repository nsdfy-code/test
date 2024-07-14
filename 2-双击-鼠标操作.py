import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

element = driver.find_element(By.ID,"userA")

element.send_keys("admin")

time.sleep(3)

action = ActionChains(driver)

action.double_click(element).perform()

time.sleep(3)

driver.quit()

