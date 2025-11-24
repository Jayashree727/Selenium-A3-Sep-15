import time
import pytest
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", "True")

driver = webdriver.Chrome(opts)

@pytest.mark.parametrize("username, pwd", [('standard_user', 'secret_sauce'), ('standard', 'secret')])
def test_login(username, pwd):
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.find_element("id", "user-name").send_keys(username)
    time.sleep(2)
    driver.find_element("id", "password").send_keys(pwd)
    time.sleep(2)
    driver.find_element("id", "login-button").click()
    time.sleep(2)


if 'inventory' in driver.current_url:
    print("successful login")
else:
    print("unsuccessful login")
