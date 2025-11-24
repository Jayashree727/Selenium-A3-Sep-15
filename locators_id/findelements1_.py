import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# print(footer_elements)      ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7,...wb22]

for ele in footer_elements:
    print(ele.text)

##############################################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
print(categories)       ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]

for ele in categories:
    print(ele.text)






















































