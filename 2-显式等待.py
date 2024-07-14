import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

element = WebDriverWait(driver,10,1).until(lambda x: x.find_element(By.CSS_SELECTOR,"input[placeholder='延时加载的输入框']"))

element.send_keys("nihao  ")

time.sleep(3)

driver.quit()

select = Select(driver.find_element(By.CSS_SELECTOR,""))


