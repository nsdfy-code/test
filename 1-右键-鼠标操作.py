import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

element = driver.find_element(By.ID,"userA")

action = ActionChains(driver)

action.context_click(element).perform()

time.sleep(3)

driver.quit()

