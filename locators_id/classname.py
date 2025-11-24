#import time
#from selenium import webdriver
#opts = webdriver.ChromeOptions()
#opts.add_experimental_option("detach", True)
#driver = webdriver.Chrome(opts)

#launch the application
#driver.get('https://demowebshop.tricentis.com/')
#time.sleep(2)

#driver.find_element("class name", "ico-register").click()
#time.sleep(2)
#driver.find_element("class name", "ico-login").click()
#time.sleep(2)
#driver.find_element("class name", "ico-cart").click()
#time.sleep(2)


#########################################
import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element("class name", "inputtext._58mg._5dba._2ph-").send_keys("shrishail")
time.sleep(2)