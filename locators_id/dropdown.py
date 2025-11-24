import time
from selenium import webdriver
#from selenium.webdriver.support.select
# import select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
#
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# drop_down = driver.find_element("xpath", '//select[@id="day"]')
# ssd = Select(drop_down)
# ssd.select_by_index(26)

#######month drop down######


#import time
# from selenium import webdriver
# from selenium.webdriver.support.select
# import select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
#
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# drop_down = driver.find_element("id", "month")
# ssd = Select(drop_down)
# ssd.select_by_value(7)

##########################year

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
#
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
# year_dd = driver.find_element("id", "year")
# ssd = Select(year_dd)
# ssd.select_by_visible_text("2022")


##############qspiders#######
#multi select dropdown
#facebook dd
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)



driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)
day = driver.find_element("id", "day")
dd = Select(day)
data = dd.options
# month = driver.find_element("id", "month")
# dd = Select(month)
# data = dd.options
# l = []
# for i in data:
#     if i.text[0] in 'aeiouAEIOU':
#         l.append(i.text)
#         print(l)



l = []  # to store odd day numbers

for i in data:
    try:
        day_num = int(i.text)
        if day_num % 2 != 0:  # check for odd number
            l.append(day_num)
    except ValueError:
        pass  # skip if text is not a number (like "Day" placeholder)

print(l)
