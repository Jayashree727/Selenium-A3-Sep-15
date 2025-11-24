#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)

#launch the application
#driver.get('https://demowebshop.tricentis.com/')
#time.sleep(2)

#driver.find_element("partial link text", "Books").click()
#time.sleep(2)
#driver.find_element("partial link text", "Computers").click()
#time.sleep(2)
#driver.find_element("partial link text", "Apparel & ").click()
#time.sleep(2)

#####################################

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.kushals.com/')
time.sleep(2)

driver.find_element("partial link text", "Bangles").click()
time.sleep(2)
driver.find_element("partial link text", "Wedding Store").click()
time.sleep(2)
driver.find_element("partial link text", "Happy Customers").click()
time.sleep(2)
driver.find_element("partial link text", "Careers").click()
time.sleep(2)