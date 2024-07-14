'''
如果你正在使用Selenium进行自动化测试或网页自动化操作，并且你的项目依赖于较新的浏览器和WebDriver
建议升级到Selenium 4并使用其推荐的元素定位方式。这将有助于你避免未来的兼容性问题
并充分利用Selenium 4提供的新功能和改进
'''
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/Nsdfy/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")

driver.find_element(By.XPATH,"/html/body/div/fieldset/form/p[1]/input").send_keys("admin")

time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="passwordA"]').send_keys("123456")

time.sleep(5)

webdriver.quit()



