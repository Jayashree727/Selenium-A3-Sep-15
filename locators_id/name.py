import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.instagram.com/')
time.sleep(2)

driver.find_element("name", "username").send_keys("jass")
time.sleep(2)
driver.find_element("name", "password").send_keys("jass@gmail.com")
time.sleep(2)


############################
#eg2:

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element("name", "firstname").send_keys("harry")
time.sleep(2)
driver.find_element("name", "lastname").send_keys("porter")
time.sleep(2)
driver.find_element("name", "reg_email__").send_keys("harryporter@gmail.com")
time.sleep(2)
driver.find_element("name", "reg_passwd__").send_keys("harry@1234")
time.sleep(2)