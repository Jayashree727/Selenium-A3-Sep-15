import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element("id", "name").send_keys("jass")
time.sleep(2)
driver.find_element("id", "email").send_keys("jass@gmail.com")
time.sleep(2)
driver.find_element("id", "phone").send_keys("7867564454")
time.sleep(2)
driver.find_element("id", "textarea").send_keys("Bangalore")
time.sleep(2)
driver.find_element("id", "female").click()
time.sleep(2)
driver.find_element("id", "friday").click()
time.sleep(2)