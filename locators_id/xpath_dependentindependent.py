import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.python.org/')
time.sleep(2)

driver.find_element("xpath", '(//a[(text(),"Downloads"])[1]').click()
time.sleep(2)
driver.find_element("xpath", '(//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()
time.sleep(2)
