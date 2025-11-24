import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.iforex.in/tools/live-rates')
time.sleep(2)

driver.find_element("xpath", '//div[text()="Gold"]/../..//span[2]').click()
time.sleep(2)
driver.find_element("xpath", '//div[text()="Gold"]/../..//span[2]').click()
time.sleep(2)