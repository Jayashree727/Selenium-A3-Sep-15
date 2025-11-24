import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element("xpath", 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys("standard_user")
time.sleep(2)
driver.find_element("xpath", 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys("secret_sauce")
time.sleep(2)
driver.find_element("xpath", 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()
time.sleep(2)
