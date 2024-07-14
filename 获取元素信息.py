from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

print(driver.find_element(By.ID, "userA").size)
print(driver.find_element(By.CSS_SELECTOR,"#fw").text)
print(driver.find_element(By.CSS_SELECTOR, "a").get_attribute("href"))
print(driver.find_element(By.CSS_SELECTOR, "span").is_displayed())
print(driver.find_element(By.ID, "cancelA").is_enabled())

print(driver.find_element(By.CSS_SELECTOR, "#jza").is_selected())

driver.quit()

