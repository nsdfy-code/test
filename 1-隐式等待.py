import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='延时加载的输入框']").send_keys("hh")

time.sleep(3)

driver.quit()