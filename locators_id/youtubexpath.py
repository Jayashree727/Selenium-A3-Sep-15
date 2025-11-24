import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.youtube.com/')
time.sleep(2)



driver.find_element("xpath", '//input[@name="search_query"]').send_keys("qspiders")
time.sleep(2)
driver.find_element("xpath", '//button[@title="Search"]').click()
time.sleep(2)