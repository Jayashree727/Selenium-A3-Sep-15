#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)

#launch the application
#driver.get('https://www.facebook.com/r.php?entry_point=login')
#time.sleep(2)

#driver.find_element("css selector", 'input[name="firstname"]').send_keys("harry")
#time.sleep(2)
#driver.find_element("css selector", 'input[name="lastname"]').send_keys("porter")
#time.sleep(2)
#driver.find_element("css selector", 'input[name="reg_email__"]').send_keys("harryporter@gmail.com")
#time.sleep(2)
#driver.find_element("css selector", 'input[name="reg_passwd__"]').send_keys("harry@1234")
#time.sleep(2)
###############################################################

import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element("css selector", 'input[class="form-control"]').send_keys("harry")
time.sleep(2)
driver.find_element("css selector", 'input[class="form-control"]').send_keys("porter@gmail.com")
time.sleep(2)



