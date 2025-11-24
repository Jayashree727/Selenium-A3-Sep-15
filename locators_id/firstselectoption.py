import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)



driver.get("file:///C:/Users/jayashree/Downloads/dd.html")
time.sleep(2)
# deserts_dd = driver.find_element("id", "a2")
# msd = Select(deserts_dd)
# msd.select_by_index(4)
# msd.select_by_index(2)
# msd.select_by_index(0)
# data = msd.first_selected_option
# print(data.text)

deserts_dd = driver.find_element("id", "a2")
msd = Select(deserts_dd)
msd.select_by_index(0)
msd.select_by_index(2)
msd.select_by_index(4)
data = msd.all_selected_options
print(data)


