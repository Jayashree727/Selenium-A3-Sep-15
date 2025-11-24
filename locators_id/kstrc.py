# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
#
#
# driver.get('https://www.ksrtc.in/')
# driver.implicitly_wait(10)
# driver.find_element("xpath","//div[@id='fromCity_chosen']").click()
# time.sleep(3)
# data = driver.find_elements("xpath","//li[@class='active-result']")
#
# for i in data:
#     print(i.text)
#
#flipkart


# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)



# driver.get('https://www.flipkart.com/')
# time.sleep(2)
# driver.find_element("name", "q").send_keys("iphone")
# time.sleep(2)

# data = driver.find_elements("xpath","//div[@class='YGcVZO _2VHNef']")
# time.sleep(2)

# option = input("Enter your Option:").lower()
# time.sleep(3)
# for i in data:
#     if i.text == option:
#         i.click()
#         break

##############redbus

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)


driver.get('https://www.redbus.in/')
time.sleep(2)
driver.find_element('xpath','//div[text()="Madiwala, Bangalore"]').send_keys('madiwala')
#driver.find_element('xpath','//div[@class="srcDest___aa6db3"]').click()

#driver.find_element("xpath",'//div[text()="KBS Luxury Bus"]/ancestor::div[@class="busTitleWrapper___ef6aa4 busTitle___749e4c"]/preceding-sibling::div[@class="timeAndSeatsWrapper___c82146 timeSeats___c91c1a"]/descendant::p[text()="20:15"]/ancestor::li[@class="tupleWrapper___da903c undefined animate__ind-search-styles-module-scss-PfFt3    "]/descendant::button[@class="primaryButton___3262c2 viewSeatsBtn___3f5f2a "]').click()