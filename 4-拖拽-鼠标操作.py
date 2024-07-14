import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/drag.html")

action = ActionChains(driver)

source = driver.find_element(By.ID,"div1")

target = driver.find_element(By.ID,"div2")

action.drag_and_drop(source,target).perform()

time.sleep(3)

driver.quit()

