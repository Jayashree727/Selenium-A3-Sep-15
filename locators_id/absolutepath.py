import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element("xpath", '//a[@data-group="women"]').click()
time.sleep(2)
driver.find_element("xpath", '//a[@data-group="home"]').click()
time.sleep(2)
driver.find_element("xpath", '//a[@data-group="genz"]').click()
time.sleep(2)

#driver.find_element("xpath", '//input[@aria-label="Mobile Number or Email"]').send_keys("harry@gmail.com")
#time.sleep(2)
#driver.find_element("xpath", '//input[@name="password"]').send_keys("secret_sauce")
###time.sleep(2)
#driver.find_element("xpath", '//input[@name="fullName"]').send_keys("harry porter")
#time.sleep(2)
#driver.find_element("xpath", '//input[@name="username"]').send_keys("harryp")
#time.sleep(2)


