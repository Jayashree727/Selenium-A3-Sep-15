import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element("link text", "Register").click()
time.sleep(2)
driver.find_element("link text", "Log in").click()
time.sleep(2)

#################################################

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.myntra.com/')
time.sleep(2)

driver.find_element("link text", "Women").click()
time.sleep(2)
driver.find_element("link text", "Home").click()
time.sleep(2)
driver.find_element("link text", "Genz").click()
time.sleep(2)

####################
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element("link text", "Women").click()
time.sleep(2)
driver.find_element("link text", "Home").click()
time.sleep(2)
driver.find_element("link text", "Genz").click()
time.sleep(2)