import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get('https://www.myntra.com/')
time.sleep(3)

#maximize browser
driver.maximize_window()
time.sleep(2)


#to go back
driver.back()
time.sleep(3)

#to go forward
driver.forward()
time.sleep(3)

#to refresh
driver.refresh()
time.sleep(3)

#fullscreen window
driver.fullscreen_window()
time.sleep(2)

#current url
print(driver.current_url)

#title
print(driver.title)

#name
print(driver.name)

#to save screenshot in same location as our python file
driver.save_screenshot('mynt_ss.png')

#to save screenshot in a directory
driver.save_screenshot(r'C:\Users\jayashree\PycharmProjects\selenium_training\screenshots\myn_ss.png')

