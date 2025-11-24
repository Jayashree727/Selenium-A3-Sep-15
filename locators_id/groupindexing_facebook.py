import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)

driver.find_element('xpath','(//input[@class="inputtext _58mg _5dba _2ph-"])[1]').send_keys('mass')
driver.find_element('xpath','(//input[@class="inputtext _58mg _5dba _2ph-"])[2]').send_keys('massy')
driver.find_element('xpath','(//input[@class="inputtext _58mg _5dba _2ph-"])[5]').send_keys('mass@gmail.com')
driver.find_element('xpath','(//input[@class="inputtext _58mg _5dba _2ph-"])[7]').send_keys('mass@123434')