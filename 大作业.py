import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

driver.find_element(By.ID,"userA").send_keys("admin")
driver.find_element(By.ID,"passwordA").send_keys("123456")
driver.find_element(By.ID,"telA").send_keys("18611111111")
driver.find_element(By.CLASS_NAME,"emailA").send_keys("123@qq.com")

time.sleep(3)

driver.find_element(By.ID,"telA").clear()

time.sleep(3)

driver.find_element(By.ID,"telA").send_keys("18600000000")

time.sleep(3)

# driver.find_element(By.CSS_SELECTOR,"button").click()
driver.find_element(By.CSS_SELECTOR,"body > div > fieldset > form > p:nth-child(5) > button").click()

time.sleep(3)

driver.quit()



