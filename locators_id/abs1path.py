import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.flipkart.com/')
time.sleep(2)

driver.find_element("xpath", '//span[text()="Mobiles & Tablets"]').click()
time.sleep(2)
driver.find_element("xpath", '//a[text()="Become a Seller"]').click()
time.sleep(2)
driver.find_element("xpath", '//button[text()="Start Selling"]').click()
time.sleep(2)