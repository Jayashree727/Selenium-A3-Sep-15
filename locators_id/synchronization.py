# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(45)
#
# driver.get(r'C:\Users\jayashree\PycharmProjects\selenium_training\progressbar (1).html')
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# driver.find_element('xpath', '//div[text()="100%"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

#####################sauce demo##############

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 20)

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('id', 'user-name').send_keys('standard_user')
time.sleep(2)
driver.find_element('id', 'password').send_keys('secret_sauce')
time.sleep(2)
driver.find_element('id', 'login-button').click()

try:
    wait_obj.until(expected_conditions.visibility_of_element_located('xpath','//span[text()="Products"]'))
    print("Login successful")
except:
    print("unsuccessful")

